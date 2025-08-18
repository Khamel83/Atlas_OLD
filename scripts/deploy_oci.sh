#!/bin/bash

# Atlas OCI Deployment Script
# Automates deployment to Oracle Cloud Infrastructure
# Supports both development and production deployments

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DEPLOYMENT_CONFIG="${PROJECT_ROOT}/config/deployment.json"

# Default values
ENVIRONMENT="production"
INSTANCE_TYPE="VM.Standard.E2.1.Micro"  # Free tier
REGION="us-ashburn-1"
COMPARTMENT_OCID=""
SSH_KEY_PATH="$HOME/.ssh/id_rsa.pub"
DOMAIN_NAME=""
SSL_CERT_PATH=""
SSL_KEY_PATH=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[WARNING] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}"
    exit 1
}

success() {
    echo -e "${GREEN}[SUCCESS] $1${NC}"
}

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Deploy Atlas to Oracle Cloud Infrastructure

OPTIONS:
    -e, --environment ENV       Deployment environment (production|staging|development) [default: production]
    -r, --region REGION         OCI region [default: us-ashburn-1]
    -c, --compartment OCID      OCI compartment OCID
    -k, --ssh-key PATH          Path to SSH public key [default: ~/.ssh/id_rsa.pub]
    -d, --domain DOMAIN         Domain name for SSL setup
    -t, --instance-type TYPE    Instance type [default: VM.Standard.E2.1.Micro]
    --ssl-cert PATH             Path to SSL certificate
    --ssl-key PATH              Path to SSL private key
    --dry-run                   Show what would be deployed without executing
    -h, --help                  Show this help message

EXAMPLES:
    # Basic deployment to free tier instance
    $0 --compartment ocid1.compartment.oc1..xxxxx

    # Production deployment with custom domain
    $0 --environment production --domain atlas.yourdomain.com --ssl-cert /path/to/cert.pem --ssl-key /path/to/key.pem

    # Development deployment
    $0 --environment development --instance-type VM.Standard.E2.2.Micro

EOF
}

check_dependencies() {
    log "Checking dependencies..."
    
    # Check for required tools
    local deps=("oci" "docker" "ssh" "scp")
    for dep in "${deps[@]}"; do
        if ! command -v "$dep" &> /dev/null; then
            error "Required dependency '$dep' is not installed"
        fi
    done
    
    # Check OCI CLI configuration
    if ! oci iam user get --user-id "$(oci iam user list --query 'data[0].id' --raw-output)" &> /dev/null; then
        error "OCI CLI is not properly configured. Run 'oci setup config'"
    fi
    
    success "All dependencies are available"
}

validate_environment() {
    log "Validating environment configuration..."
    
    # Check required parameters
    if [[ -z "$COMPARTMENT_OCID" ]]; then
        error "Compartment OCID is required. Use --compartment option."
    fi
    
    if [[ ! -f "$SSH_KEY_PATH" ]]; then
        error "SSH public key not found at $SSH_KEY_PATH"
    fi
    
    # Validate environment files
    local env_file="${PROJECT_ROOT}/.env.${ENVIRONMENT}"
    if [[ ! -f "$env_file" ]]; then
        warn "Environment file $env_file not found. Creating from template..."
        cp "${PROJECT_ROOT}/.env.example" "$env_file"
    fi
    
    success "Environment validation complete"
}

create_instance() {
    log "Creating OCI compute instance..."
    
    local instance_name="atlas-${ENVIRONMENT}-$(date +%s)"
    local shape="$INSTANCE_TYPE"
    local image_id
    
    # Get latest Ubuntu image ID
    image_id=$(oci compute image list \
        --compartment-id "$COMPARTMENT_OCID" \
        --operating-system "Canonical Ubuntu" \
        --shape "$shape" \
        --limit 1 \
        --query 'data[0].id' \
        --raw-output)
    
    if [[ -z "$image_id" || "$image_id" == "null" ]]; then
        error "Failed to find suitable Ubuntu image for shape $shape"
    fi
    
    # Create the instance
    local instance_ocid
    instance_ocid=$(oci compute instance launch \
        --compartment-id "$COMPARTMENT_OCID" \
        --availability-domain "$(oci iam availability-domain list --compartment-id "$COMPARTMENT_OCID" --query 'data[0].name' --raw-output)" \
        --shape "$shape" \
        --image-id "$image_id" \
        --ssh-authorized-keys-file "$SSH_KEY_PATH" \
        --display-name "$instance_name" \
        --wait-for-state RUNNING \
        --query 'data.id' \
        --raw-output)
    
    if [[ -z "$instance_ocid" ]]; then
        error "Failed to create instance"
    fi
    
    # Get instance IP
    local public_ip
    public_ip=$(oci compute instance list-vnics \
        --instance-id "$instance_ocid" \
        --query 'data[0]."public-ip"' \
        --raw-output)
    
    echo "$instance_ocid" > "${PROJECT_ROOT}/.instance_ocid"
    echo "$public_ip" > "${PROJECT_ROOT}/.instance_ip"
    
    success "Instance created: $instance_name ($public_ip)"
    log "Instance OCID: $instance_ocid"
}

setup_security_rules() {
    log "Setting up security rules..."
    
    # Get default VCN and security list
    local vcn_id
    vcn_id=$(oci network vcn list \
        --compartment-id "$COMPARTMENT_OCID" \
        --query 'data[0].id' \
        --raw-output)
    
    local security_list_id
    security_list_id=$(oci network security-list list \
        --compartment-id "$COMPARTMENT_OCID" \
        --vcn-id "$vcn_id" \
        --query 'data[0].id' \
        --raw-output)
    
    # Add ingress rules for Atlas
    oci network security-list update \
        --security-list-id "$security_list_id" \
        --ingress-security-rules '[
            {
                "protocol": "6",
                "source": "0.0.0.0/0",
                "tcp-options": {
                    "destination-port-range": {
                        "min": 80,
                        "max": 80
                    }
                }
            },
            {
                "protocol": "6", 
                "source": "0.0.0.0/0",
                "tcp-options": {
                    "destination-port-range": {
                        "min": 443,
                        "max": 443
                    }
                }
            },
            {
                "protocol": "6",
                "source": "0.0.0.0/0", 
                "tcp-options": {
                    "destination-port-range": {
                        "min": 5000,
                        "max": 5000
                    }
                }
            }
        ]' \
        --force || warn "Security rules may already exist"
    
    success "Security rules configured"
}

deploy_application() {
    log "Deploying Atlas application..."
    
    local instance_ip
    instance_ip=$(cat "${PROJECT_ROOT}/.instance_ip")
    
    # Wait for instance to be accessible
    log "Waiting for instance to be accessible..."
    local retries=30
    while ! ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "ubuntu@$instance_ip" "echo 'connected'" &> /dev/null; do
        if [[ $retries -eq 0 ]]; then
            error "Instance is not accessible via SSH"
        fi
        sleep 10
        ((retries--))
    done
    
    # Copy application files
    log "Copying application files..."
    rsync -avz --exclude='.git' --exclude='__pycache__' --exclude='*.pyc' \
        "$PROJECT_ROOT/" "ubuntu@$instance_ip:~/atlas/"
    
    # Copy environment configuration
    scp "${PROJECT_ROOT}/.env.${ENVIRONMENT}" "ubuntu@$instance_ip:~/atlas/.env"
    
    # Run deployment commands on remote instance
    ssh -o StrictHostKeyChecking=no "ubuntu@$instance_ip" << 'EOF'
        set -euo pipefail
        
        # Update system
        sudo apt-get update && sudo apt-get upgrade -y
        
        # Install Docker
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        
        # Install Docker Compose
        sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose
        
        # Setup Atlas
        cd ~/atlas
        
        # Build and start containers
        docker-compose up -d
        
        # Configure systemd service for auto-start
        sudo tee /etc/systemd/system/atlas.service > /dev/null << SYSTEMD_EOF
[Unit]
Description=Atlas Personal Knowledge System
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/ubuntu/atlas
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0
User=ubuntu

[Install]
WantedBy=multi-user.target
SYSTEMD_EOF
        
        sudo systemctl enable atlas.service
        sudo systemctl start atlas.service
        
        echo "Atlas deployment complete"
EOF
    
    success "Application deployed successfully"
}

setup_ssl() {
    if [[ -z "$DOMAIN_NAME" ]]; then
        log "No domain specified, skipping SSL setup"
        return
    fi
    
    log "Setting up SSL for domain: $DOMAIN_NAME"
    
    local instance_ip
    instance_ip=$(cat "${PROJECT_ROOT}/.instance_ip")
    
    if [[ -n "$SSL_CERT_PATH" && -n "$SSL_KEY_PATH" ]]; then
        # Use provided certificates
        scp "$SSL_CERT_PATH" "ubuntu@$instance_ip:~/atlas/docker/nginx/ssl/cert.pem"
        scp "$SSL_KEY_PATH" "ubuntu@$instance_ip:~/atlas/docker/nginx/ssl/key.pem"
    else
        # Use Let's Encrypt
        ssh -o StrictHostKeyChecking=no "ubuntu@$instance_ip" << EOF
            # Install certbot
            sudo apt-get install -y certbot python3-certbot-nginx
            
            # Get certificate
            sudo certbot --nginx -d $DOMAIN_NAME --non-interactive --agree-tos --email admin@$DOMAIN_NAME
            
            # Copy certificates to Docker volume
            sudo mkdir -p ~/atlas/docker/nginx/ssl
            sudo cp /etc/letsencrypt/live/$DOMAIN_NAME/fullchain.pem ~/atlas/docker/nginx/ssl/cert.pem
            sudo cp /etc/letsencrypt/live/$DOMAIN_NAME/privkey.pem ~/atlas/docker/nginx/ssl/key.pem
            sudo chown ubuntu:ubuntu ~/atlas/docker/nginx/ssl/*
EOF
    fi
    
    # Enable SSL in docker-compose
    ssh -o StrictHostKeyChecking=no "ubuntu@$instance_ip" << 'EOF'
        cd ~/atlas
        docker-compose --profile production up -d
EOF
    
    success "SSL configured for $DOMAIN_NAME"
}

generate_deployment_summary() {
    log "Generating deployment summary..."
    
    local instance_ip
    instance_ip=$(cat "${PROJECT_ROOT}/.instance_ip")
    
    cat > "${PROJECT_ROOT}/deployment_summary.txt" << EOF
Atlas Deployment Summary
========================

Environment: $ENVIRONMENT
Instance IP: $instance_ip
Instance Type: $INSTANCE_TYPE
Region: $REGION

Access URLs:
- Main Application: http://$instance_ip:5000
- Capture API: http://$instance_ip:5000/api/capture
EOF

    if [[ -n "$DOMAIN_NAME" ]]; then
        cat >> "${PROJECT_ROOT}/deployment_summary.txt" << EOF
- Domain: https://$DOMAIN_NAME
EOF
    fi

    cat >> "${PROJECT_ROOT}/deployment_summary.txt" << EOF

SSH Access:
ssh ubuntu@$instance_ip

Management Commands:
- Check status: ssh ubuntu@$instance_ip 'cd atlas && docker-compose ps'
- View logs: ssh ubuntu@$instance_ip 'cd atlas && docker-compose logs -f'
- Restart: ssh ubuntu@$instance_ip 'cd atlas && docker-compose restart'

Files:
- Instance OCID: .instance_ocid
- Instance IP: .instance_ip
- Environment: .env.$ENVIRONMENT
EOF

    success "Deployment summary saved to deployment_summary.txt"
}

cleanup() {
    log "Cleaning up temporary files..."
    rm -f "${PROJECT_ROOT}/.instance_ocid" "${PROJECT_ROOT}/.instance_ip"
}

main() {
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -e|--environment)
                ENVIRONMENT="$2"
                shift 2
                ;;
            -r|--region)
                REGION="$2"
                shift 2
                ;;
            -c|--compartment)
                COMPARTMENT_OCID="$2"
                shift 2
                ;;
            -k|--ssh-key)
                SSH_KEY_PATH="$2"
                shift 2
                ;;
            -d|--domain)
                DOMAIN_NAME="$2"
                shift 2
                ;;
            -t|--instance-type)
                INSTANCE_TYPE="$2"
                shift 2
                ;;
            --ssl-cert)
                SSL_CERT_PATH="$2"
                shift 2
                ;;
            --ssl-key)
                SSL_KEY_PATH="$2"
                shift 2
                ;;
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            *)
                error "Unknown option: $1"
                ;;
        esac
    done
    
    # Validate environment
    if [[ ! "$ENVIRONMENT" =~ ^(production|staging|development)$ ]]; then
        error "Invalid environment: $ENVIRONMENT. Must be production, staging, or development"
    fi
    
    log "Starting Atlas deployment to OCI"
    log "Environment: $ENVIRONMENT"
    log "Region: $REGION"
    log "Instance Type: $INSTANCE_TYPE"
    
    if [[ "${DRY_RUN:-false}" == "true" ]]; then
        log "DRY RUN - No actual deployment will occur"
        return 0
    fi
    
    # Execute deployment steps
    check_dependencies
    validate_environment
    create_instance
    setup_security_rules
    deploy_application
    setup_ssl
    generate_deployment_summary
    
    success "Atlas deployment completed successfully!"
    success "Instance IP: $(cat "${PROJECT_ROOT}/.instance_ip")"
    success "View full summary in deployment_summary.txt"
}

# Trap cleanup on exit
trap cleanup EXIT

# Run main function
main "$@"