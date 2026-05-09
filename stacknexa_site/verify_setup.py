#!/usr/bin/env python
"""
StackNexaSolutions - Installation Verification Script
Run this script to verify your setup is correct
"""

import os
import sys
import django

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{text.center(60)}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{'='*60}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ {text}{Colors.END}")

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print_success(f"Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print_error(f"Python version: {version.major}.{version.minor}.{version.micro} (3.8+ required)")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = {
        'django': 'Django',
        'openai': 'OpenAI',
        'dotenv': 'python-dotenv'
    }
    
    all_installed = True
    for package, name in required_packages.items():
        try:
            __import__(package)
            print_success(f"{name} is installed")
        except ImportError:
            print_error(f"{name} is NOT installed")
            all_installed = False
    
    return all_installed

def check_env_file():
    """Check if .env file exists and has required variables"""
    if not os.path.exists('.env'):
        print_warning(".env file not found")
        print_info("Copy .env.example to .env and add your OpenAI API key")
        return False
    
    print_success(".env file exists")
    
    # Check for API key
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key != 'your_openai_api_key_here':
        print_success("OpenAI API key is configured")
        return True
    else:
        print_warning("OpenAI API key not configured (chatbot will use fallback responses)")
        return True

def check_django_setup():
    """Check Django configuration"""
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stacknexa_site.settings')
        django.setup()
        print_success("Django settings loaded successfully")
        return True
    except Exception as e:
        print_error(f"Django setup failed: {e}")
        return False

def check_database():
    """Check if database is set up"""
    if os.path.exists('db.sqlite3'):
        print_success("Database file exists")
        
        # Check if migrations are applied
        from django.core.management import execute_from_command_line
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                if len(tables) > 0:
                    print_success(f"Database has {len(tables)} tables")
                    return True
                else:
                    print_warning("Database exists but has no tables")
                    print_info("Run: python manage.py migrate")
                    return False
        except Exception as e:
            print_error(f"Database check failed: {e}")
            return False
    else:
        print_warning("Database file not found")
        print_info("Run: python manage.py migrate")
        return False

def check_static_files():
    """Check if static files exist"""
    static_dir = 'main/static/main'
    required_files = [
        'css/styles.css',
        'js/main.js'
    ]
    
    all_exist = True
    for file in required_files:
        filepath = os.path.join(static_dir, file)
        if os.path.exists(filepath):
            print_success(f"Found: {file}")
        else:
            print_error(f"Missing: {file}")
            all_exist = False
    
    return all_exist

def check_templates():
    """Check if template files exist"""
    template_dir = 'main/templates/main'
    required_templates = [
        'base.html',
        'home.html',
        'about.html',
        'services.html',
        'portfolio.html',
        'contact.html'
    ]
    
    all_exist = True
    for template in required_templates:
        filepath = os.path.join(template_dir, template)
        if os.path.exists(filepath):
            print_success(f"Found: {template}")
        else:
            print_error(f"Missing: {template}")
            all_exist = False
    
    return all_exist

def main():
    """Main verification function"""
    print_header("StackNexaSolutions - Installation Verification")
    
    print(f"{Colors.BOLD}Checking system requirements...{Colors.END}\n")
    
    checks = {
        "Python Version": check_python_version(),
        "Required Packages": check_dependencies(),
        "Environment File": check_env_file(),
        "Django Configuration": check_django_setup(),
        "Database": check_database(),
        "Static Files": check_static_files(),
        "Templates": check_templates()
    }
    
    print_header("Verification Summary")
    
    passed = sum(checks.values())
    total = len(checks)
    
    for check_name, result in checks.items():
        status = f"{Colors.GREEN}✓ PASS{Colors.END}" if result else f"{Colors.RED}✗ FAIL{Colors.END}"
        print(f"{check_name:.<40} {status}")
    
    print(f"\n{Colors.BOLD}Results: {passed}/{total} checks passed{Colors.END}\n")
    
    if passed == total:
        print_success("All checks passed! Your installation is ready.")
        print_info("\nNext steps:")
        print("  1. Run: python manage.py runserver")
        print("  2. Visit: http://127.0.0.1:8000/")
        print("  3. Test the chatbot and contact form")
        print("  4. Access admin panel: http://127.0.0.1:8000/admin/")
    else:
        print_warning("Some checks failed. Please fix the issues above.")
        print_info("\nCommon solutions:")
        print("  • Install packages: pip install -r requirements.txt")
        print("  • Create .env: cp .env.example .env")
        print("  • Run migrations: python manage.py migrate")
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}\n")

if __name__ == '__main__':
    main()
