#!/usr/bin/env python
"""
StackNexaSolutions - Automated Setup Script
Helps you get started quickly with minimal manual steps
"""

import os
import sys
import subprocess
import secrets

def print_header(text):
    print("\n" + "=" * 60)
    print(text.center(60))
    print("=" * 60 + "\n")

def print_step(number, text):
    print(f"\n🔹 Step {number}: {text}")

def run_command(command, description):
    """Run a shell command and show output"""
    print(f"   Running: {description}...")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True
        )
        print(f"   ✓ Success!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ✗ Error: {e.stderr}")
        return False

def create_env_file():
    """Create .env file from template"""
    if os.path.exists('.env'):
        response = input("   .env file already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("   Skipping .env creation")
            return
    
    # Generate a secure secret key
    secret_key = secrets.token_urlsafe(50)
    
    env_content = f"""# StackNexaSolutions Environment Variables
# Created by setup script

# IMPORTANT: Add your OpenAI API key here!
# Get it from: https://platform.openai.com/api-keys
OPENAI_API_KEY=your_openai_api_key_here

# Django Settings
SECRET_KEY={secret_key}
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (default SQLite - change for production)
# DATABASE_URL=postgres://user:password@localhost:5432/dbname

# Email Configuration (optional)
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("   ✓ Created .env file with secure SECRET_KEY")
    print("   ⚠  Remember to add your OPENAI_API_KEY!")

def main():
    print_header("StackNexaSolutions - Automated Setup")
    
    print("""
This script will help you set up your StackNexaSolutions website.
It will:
  1. Install Python dependencies
  2. Create environment file (.env)
  3. Run database migrations
  4. Offer to create admin user
  5. Test the setup
  
Press Enter to continue or Ctrl+C to cancel...
    """)
    input()
    
    # Step 1: Install Dependencies
    print_step(1, "Installing Python Dependencies")
    if not os.path.exists('requirements.txt'):
        print("   ✗ Error: requirements.txt not found!")
        print("   Are you in the correct directory?")
        sys.exit(1)
    
    run_command(
        'pip install -r requirements.txt',
        'Installing packages'
    )
    
    # Step 2: Create .env file
    print_step(2, "Creating Environment File")
    create_env_file()
    
    # Step 3: Run Migrations
    print_step(3, "Setting Up Database")
    run_command(
        'python manage.py migrate',
        'Running database migrations'
    )
    
    # Step 4: Create Superuser (optional)
    print_step(4, "Create Admin User")
    response = input("   Do you want to create an admin user now? (Y/n): ")
    
    if response.lower() != 'n':
        print("   Follow the prompts to create your admin account:")
        subprocess.run('python manage.py createsuperuser', shell=True)
    else:
        print("   Skipped. You can create one later with:")
        print("   python manage.py createsuperuser")
    
    # Step 5: Verify Setup
    print_step(5, "Verifying Installation")
    
    if os.path.exists('verify_setup.py'):
        print("   Running verification script...")
        subprocess.run('python verify_setup.py', shell=True)
    else:
        print("   ✓ Setup appears complete!")
    
    # Final Instructions
    print_header("Setup Complete! 🎉")
    
    print("""
✅ Your StackNexaSolutions website is ready!

📝 IMPORTANT NEXT STEPS:

1. Add your OpenAI API key to .env file:
   - Edit .env
   - Replace 'your_openai_api_key_here' with your actual key
   - Get key from: https://platform.openai.com/api-keys

2. Start the development server:
   python manage.py runserver

3. Open your browser to:
   http://127.0.0.1:8000/

4. Test the chatbot:
   - Click the chat icon (bottom-right)
   - Try asking about services

5. Access admin panel:
   http://127.0.0.1:8000/admin/
   (Use the credentials you just created)

📚 Documentation:
   - QUICKSTART.md - Quick reference
   - README.md - Full documentation
   - CUSTOMIZATION.md - How to customize
   - DEPLOYMENT.md - Deploy to production

🚀 Ready to launch!
    """)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Setup failed with error: {e}")
        sys.exit(1)
