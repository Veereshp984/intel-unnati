#!/usr/bin/env python3
"""
Easy setup script for Smart Product Labeling Backend
Run this script to set up everything automatically
"""

import os
import subprocess
import sys
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        else:
            result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python():
    """Check if Python is installed and version is adequate"""
    print("🔍 Checking Python installation...")
    python_version = sys.version_info
    if python_version.major == 3 and python_version.minor >= 8:
        print(f"✅ Python {python_version.major}.{python_version.minor} found!")
        return True
    else:
        print("❌ Python 3.8+ is required!")
        return False

def create_virtual_environment():
    """Create a virtual environment"""
    if not os.path.exists('venv'):
        if platform.system() == "Windows":
            return run_command("python -m venv venv", "Creating virtual environment")
        else:
            return run_command("python3 -m venv venv", "Creating virtual environment")
    else:
        print("✅ Virtual environment already exists!")
        return True

def activate_and_install():
    """Install requirements in virtual environment"""
    if platform.system() == "Windows":
        pip_path = "venv\\Scripts\\pip.exe"
        python_path = "venv\\Scripts\\python.exe"
    else:
        pip_path = "venv/bin/pip"
        python_path = "venv/bin/python"
    
    # Install requirements
    if run_command(f"{pip_path} install -r requirements.txt", "Installing Python packages"):
        return True
    return False

def setup_database():
    """Initialize the database"""
    if platform.system() == "Windows":
        python_path = "venv\\Scripts\\python.exe"
    else:
        python_path = "venv/bin/python"
    
    print("\n🔄 Setting up database...")
    
    # Create the database initialization script
    init_script = '''
from app import app, db
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
'''
    
    with open('init_db.py', 'w') as f:
        f.write(init_script)
    
    success = run_command(f"{python_path} init_db.py", "Initializing database")
    
    # Clean up
    if os.path.exists('init_db.py'):
        os.remove('init_db.py')
    
    return success

def create_run_script():
    """Create a run script for easy startup"""
    if platform.system() == "Windows":
        run_script = '''@echo off
echo Starting Smart Product Labeling Backend...
venv\\Scripts\\python.exe app.py
pause
'''
        with open('run.bat', 'w') as f:
            f.write(run_script)
        print("✅ Created run.bat - double-click to start the server!")
    else:
        run_script = '''#!/bin/bash
echo "Starting Smart Product Labeling Backend..."
venv/bin/python app.py
'''
        with open('run.sh', 'w') as f:
            f.write(run_script)
        os.chmod('run.sh', 0o755)
        print("✅ Created run.sh - run './run.sh' to start the server!")

def main():
    """Main setup function"""
    print("🚀 Smart Product Labeling Backend Setup")
    print("=" * 50)
    
    # Check Python
    if not check_python():
        return False
    
    # Create virtual environment
    if not create_virtual_environment():
        return False
    
    # Install packages
    if not activate_and_install():
        return False
    
    # Setup database
    if not setup_database():
        return False
    
    # Create run script
    create_run_script()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit the .env file with your configuration")
    print("2. Start the server:")
    if platform.system() == "Windows":
        print("   - Double-click run.bat, or")
        print("   - Run: venv\\Scripts\\python app.py")
    else:
        print("   - Run: ./run.sh, or")
        print("   - Run: venv/bin/python app.py")
    print("3. Open http://localhost:5000 in your browser")
    print("4. API endpoints are available at http://localhost:5000/api/")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Setup failed! Please check the errors above.")
        sys.exit(1)