#!/usr/bin/env python
"""
Quick deployment test script
Run this to verify your app is deployment-ready
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and return the result"""
    print(f"🔍 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - PASSED")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False

def check_files():
    """Check if required files exist"""
    required_files = [
        'manage.py',
        'requirements.txt',
        'travel_booking/settings.py',
        'Procfile',
        'runtime.txt',
        'Dockerfile',
    ]
    
    print("📁 Checking required files...")
    all_files_exist = True
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Missing")
            all_files_exist = False
    
    return all_files_exist

def main():
    print("🚀 Travel Booking App - Deployment Readiness Test")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path('manage.py').exists():
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    test_results = []
    
    # Check required files
    test_results.append(check_files())
    
    # Check Django installation
    test_results.append(run_command(
        "python -c 'import django; print(f\"Django {django.get_version()}\")'",
        "Django installation"
    ))
    
    # Check project structure
    test_results.append(run_command(
        "python manage.py check",
        "Django project structure"
    ))
    
    # Check if we can collect static files
    test_results.append(run_command(
        "python manage.py collectstatic --noinput --dry-run",
        "Static files collection (dry run)"
    ))
    
    # Check for deployment security
    test_results.append(run_command(
        "python manage.py check --deploy --fail-level WARNING",
        "Deployment security check (will show warnings)"
    ))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 DEPLOYMENT READINESS SUMMARY")
    print("=" * 50)
    
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! Your app is ready for deployment!")
    else:
        print(f"⚠️ {total_tests - passed_tests} test(s) failed. Please fix the issues above.")
    
    print("\n📋 Next Steps:")
    print("1. Create .env file with production values")
    print("2. Generate a secure SECRET_KEY")
    print("3. Set DEBUG=False for production")
    print("4. Configure ALLOWED_HOSTS for your domain")
    print("5. Choose your deployment platform and follow the guide")
    
    print("\n📚 Documentation:")
    print("- QUICK_DEPLOY.md - Quick deployment guide")
    print("- DEPLOYMENT_GUIDE.md - Detailed instructions")
    print("- DEPLOYMENT_CHECKLIST.md - Step-by-step checklist")
    print("- SECURITY_NOTES.md - Security best practices")

if __name__ == "__main__":
    main()
