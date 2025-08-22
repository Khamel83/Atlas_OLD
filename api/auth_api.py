\"\"\"
Authentication and Security API for Atlas
Provides authentication, authorization, and security features for the API.
\"\"\"

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional
import hashlib
import os
import secrets
import jwt
from datetime import datetime, timedelta

# Create router for authentication endpoints
auth_router = APIRouter(prefix=\"/auth\", tags=[\"authentication\"])

# Security scheme
security = HTTPBearer()

# Simple in-memory storage for API keys (in production, use a database)
API_KEYS = {}

# JWT configuration
SECRET_KEY = os.environ.get(\"ATLAS_JWT_SECRET\", \"atlas_default_secret_key\")
ALGORITHM = \"HS256\"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegistration(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class APIKeyCreate(BaseModel):
    name: str
    permissions: list[str] = [\"read\"]

class APIKeyResponse(BaseModel):
    key: str
    name: str
    permissions: list[str]
    created_at: str

def hash_password(password: str) -> str:
    \"\"\"Hash a password for storage\"\"\"
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    \"\"\"Verify a plain password against a hashed password\"\"\"
    return hash_password(plain_password) == hashed_password

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    \"\"\"Create a JWT access token\"\"\"
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({\"exp\": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    \"\"\"Verify JWT token\"\"\"
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=\"Invalid authentication credentials\",
            headers={\"WWW-Authenticate\": \"Bearer\"},
        )

def verify_api_key(api_key: str) -> bool:
    \"\"\"Verify API key\"\"\"
    return api_key in API_KEYS

@auth_router.post(\"/register\", response_model=Token)
async def register_user(user: UserRegistration):
    \"\"\"Register a new user\"\"\"
    # In a real implementation, you would check if the user already exists
    # and store the user in a database
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={\"sub\": user.username}, expires_delta=access_token_expires
    )
    return {\"access_token\": access_token, \"token_type\": \"bearer\"}

@auth_router.post(\"/login\", response_model=Token)
async def login_user(user: UserLogin):
    \"\"\"Login and get access token\"\"\"
    # In a real implementation, you would verify the user credentials against a database
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={\"sub\": user.username}, expires_delta=access_token_expires
    )
    return {\"access_token\": access_token, \"token_type\": \"bearer\"}

@auth_router.post(\"/api-keys\", response_model=APIKeyResponse)
async def create_api_key(
    key_data: APIKeyCreate,
    token: dict = Depends(verify_token)
):
    \"\"\"Create a new API key\"\"\"
    # Generate a new API key
    api_key = secrets.token_urlsafe(32)
    
    # Store the API key (in production, store in a database)
    API_KEYS[api_key] = {
        \"name\": key_data.name,
        \"permissions\": key_data.permissions,
        \"created_at\": datetime.utcnow().isoformat(),
        \"owner\": token.get(\"sub\")
    }
    
    return APIKeyResponse(
        key=api_key,
        name=key_data.name,
        permissions=key_data.permissions,
        created_at=API_KEYS[api_key][\"created_at\"]
    )

@auth_router.get(\"/api-keys\", response_model=list[APIKeyResponse])
async def list_api_keys(token: dict = Depends(verify_token)):
    \"\"\"List all API keys for the current user\"\"\"
    user_keys = []
    for key, data in API_KEYS.items():
        if data.get(\"owner\") == token.get(\"sub\"):
            user_keys.append(APIKeyResponse(
                key=\"*\" * len(key),  # Hide the actual key for security
                name=data[\"name\"],
                permissions=data[\"permissions\"],
                created_at=data[\"created_at\"]
            ))
    return user_keys

@auth_router.delete(\"/api-keys/{key_id}\")
async def delete_api_key(key_id: str, token: dict = Depends(verify_token)):
    \"\"\"Delete an API key\"\"\"
    # In a real implementation, you would verify ownership and delete from database
    # For this example, we'll just remove from memory
    keys_to_delete = []
    for key, data in API_KEYS.items():
        if data.get(\"owner\") == token.get(\"sub\") and key.startswith(key_id[:8]):
            keys_to_delete.append(key)
    
    for key in keys_to_delete:
        del API_KEYS[key]
    
    return {\"message\": \"API key deleted successfully\"}

# API key verification dependency
def verify_api_key_dependency(api_key: str):
    \"\"\"Dependency to verify API key in request headers\"\"\"
    if not verify_api_key(api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=\"Invalid API key\",
        )
    return API_KEYS[api_key]

# Health check for auth service
@auth_router.get(\"/health\")
async def auth_health_check():
    \"\"\"Health check for authentication service\"\"\"
    return {
        \"status\": \"healthy\",
        \"service\": \"Atlas Authentication Service\",
        \"active_api_keys\": len(API_KEYS)
    }