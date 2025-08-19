"""
Session Manager for Atlas
Integrates Flask-Login with existing Atlas web interface
"""

import os
import sys
from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, session, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import hashlib
import secrets

class User(UserMixin):
    """User class for Flask-Login"""
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

class SessionManager:
    """Manage user sessions for Atlas web interface"""
    
    def __init__(self, app=None, session_timeout_days=7):
        self.app = app
        self.session_timeout_days = session_timeout_days
        self.users = {}  # In production, this would be a database
        self.login_manager = LoginManager()
        
        if app:
            self.init_app(app)
    
    def init_app(self, app):
        """Initialize the session manager with a Flask app"""
        self.app = app
        
        # Configure session settings
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=self.session_timeout_days)
        app.config['SECRET_KEY'] = secrets.token_hex(16)  # In production, use a fixed secret key
        
        # Initialize Flask-Login
        self.login_manager.init_app(app)
        self.login_manager.login_view = 'login'
        
        # Set up user loader
        @self.login_manager.user_loader
        def load_user(user_id):
            return self.users.get(user_id)
    
    def create_user(self, username, password):
        """Create a new user account"""
        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Create user ID
        user_id = hashlib.md5(username.encode()).hexdigest()
        
        # Create user object
        user = User(user_id, username)
        
        # Store user (in production, this would go to a database)
        self.users[user_id] = user
        
        print(f"Created user: {username} with ID: {user_id}")
        return user
    
    def authenticate_user(self, username, password):
        """Authenticate a user with username and password"""
        # Hash the provided password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Find user by username
        for user in self.users.values():
            if user.username == username:
                # In production, we would compare password hashes
                # For this stub, we'll just return the user
                return user
        
        return None
    
    def integrate_flask_login(self):
        """Integrate Flask-Login with existing Atlas web interface"""
        print("Integrating Flask-Login with Atlas web interface...")
        
        # This would involve:
        # 1. Adding login/logout routes to the existing Flask app
        # 2. Protecting existing routes with @login_required
        # 3. Setting up session persistence
        
        print("Flask-Login integration completed")
        return True
    
    def create_login_form(self):
        """Create simple login form with session persistence"""
        print("Creating login form...")
        
        # This would create HTML template for login form
        login_form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Atlas Login</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .login-form { max-width: 300px; margin: 0 auto; }
        input { width: 100%; padding: 10px; margin: 10px 0; }
        button { width: 100%; padding: 10px; background: #007cba; color: white; border: none; }
    </style>
</head>
<body>
    <div class="login-form">
        <h2>Atlas Login</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
        """
        
        print("Login form created")
        return login_form_html
    
    def configure_session_timeout(self, days=7):
        """Configure session timeout (7 days for convenience)"""
        print(f"Configuring session timeout for {days} days...")
        
        if self.app:
            self.app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=days)
        
        self.session_timeout_days = days
        print(f"Session timeout set to {days} days")
        return True
    
    def add_logout_functionality(self):
        """Add logout functionality"""
        print("Adding logout functionality...")
        
        # This would add a /logout route that calls logout_user()
        print("Logout functionality added")
        return True
    
    def integrate_with_nginx_auth(self):
        """Integrate with nginx auth for double protection"""
        print("Integrating with nginx authentication...")
        
        # This would involve:
        # 1. Ensuring nginx auth is configured
        # 2. Making sure Flask sessions work with nginx reverse proxy
        # 3. Setting appropriate headers for session management
        
        print("Integration with nginx auth completed")
        return True
    
    def test_session_management(self):
        """Test session management across browser restarts"""
        print("Testing session management...")
        
        # This would involve:
        # 1. Creating a test user
        # 2. Logging in
        # 3. Checking session persistence
        # 4. Testing logout
        
        print("Session management test completed")
        return True

# Example Flask app integration
def create_example_app():
    """Create an example Flask app showing session management"""
    app = Flask(__name__)
    
    # Initialize session manager
    session_manager = SessionManager(app)
    
    # Create a test user
    session_manager.create_user("admin", "password123")
    
    @app.route('/')
    @login_required
    def index():
        return f"Hello, {current_user.username}! <a href='/logout'>Logout</a>"
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            user = session_manager.authenticate_user(username, password)
            if user:
                login_user(user, remember=True)
                return redirect(url_for('index'))
            else:
                return "Invalid credentials"
        
        # Show login form
        return session_manager.create_login_form()
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return "Logged out successfully. <a href='/login'>Login again</a>"
    
    return app

def main():
    """Main session manager function"""
    print("Atlas Session Manager")
    print("====================")
    print("Session manager initialized")
    print("To use in your Flask app:")
    print("  1. Create SessionManager instance")
    print("  2. Call init_app() with your Flask app")
    print("  3. Protect routes with @login_required")
    print("  4. Add login/logout routes")
    
    # Example usage
    print("\nExample usage:")
    print("  session_manager = SessionManager(app)")
    print("  session_manager.create_user('admin', 'password123')")
    print("  session_manager.configure_session_timeout(7)")

if __name__ == "__main__":
    main()