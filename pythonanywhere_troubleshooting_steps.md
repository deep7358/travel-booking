# 🚨 PythonAnywhere 502 Error Troubleshooting Guide

## Error: 502-backend
This means your Django app is failing to start. Let's fix it step by step.

## 🔍 **Step 1: Check Error Logs**
1. Go to PythonAnywhere **Web** tab
2. Click on **Error log** link
3. Look for recent error messages
4. Also check **Server log**

## 🔧 **Step 2: Verify File Structure**
In PythonAnywhere **Files** tab, ensure you have:
```
/home/DeepGupta/travel/
├── manage.py
├── .env (MUST CREATE THIS!)
├── requirements.txt
├── db.sqlite3
├── travel_booking/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
└── other folders...
```

## 🚨 **Step 3: Create Missing .env File**
**CRITICAL:** Create `/home/DeepGupta/travel/.env` with this content:
```
DEBUG=False
SECRET_KEY=your-generated-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,DeepGupta.pythonanywhere.com
USE_SQLITE=True
```

## 📦 **Step 4: Install Dependencies**
In PythonAnywhere **Console**:
```bash
cd /home/DeepGupta/travel
pip3.11 install --user -r requirements.txt
```

## 🗄️ **Step 5: Run Django Commands**
```bash
cd /home/DeepGupta/travel
python3.11 manage.py migrate
python3.11 manage.py collectstatic --noinput
```

## 🔑 **Step 6: Generate SECRET_KEY**
```bash
python3.11 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output and update your .env file.

## 🔧 **Step 7: Fix WSGI Configuration**
In **Web** tab → **WSGI configuration file**, use this content:
```python
import os
import sys

project_home = '/home/DeepGupta/travel'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 🗂️ **Step 8: Fix Static Files Paths**
In **Web** tab, set:
- URL: `/static/` → Directory: `/home/DeepGupta/travel/staticfiles/`
- URL: `/media/` → Directory: `/home/DeepGupta/travel/media/`

## ✅ **Step 9: Test Django Manually**
In console, test if Django works:
```bash
cd /home/DeepGupta/travel
python3.11 manage.py check
python3.11 manage.py runserver
```
Press Ctrl+C to stop the test server.

## 🔄 **Step 10: Reload Web App**
Click **"Reload"** button in Web tab.

## 🆘 **Common Error Solutions**

### Error: "No module named 'travel_booking'"
- Check WSGI file uses `travel_booking.settings`
- Verify `/home/DeepGupta/travel/travel_booking/` exists

### Error: "ImproperlyConfigured"
- Create the .env file with proper values
- Check SECRET_KEY is set

### Error: "DisallowedHost"
- Add your domain to ALLOWED_HOSTS in .env

### Error: "OperationalError"
- Run `python3.11 manage.py migrate`

### Error: "Static files not found"
- Run `python3.11 manage.py collectstatic --noinput`
- Check static files paths in Web tab

## 🔍 **Debug Commands**
```bash
# Check if project structure is correct
ls -la /home/DeepGupta/travel/

# Test Django settings
python3.11 -c "import os; os.environ['DJANGO_SETTINGS_MODULE']='travel_booking.settings'; import django; django.setup(); print('OK')"

# Check installed packages
pip3.11 list --user | grep -i django
```

## 📞 **Still Having Issues?**
If you're still getting 502 errors:
1. Check the exact error message in Error log
2. Verify all file permissions
3. Try the debug WSGI file I created earlier
4. Make sure Python version matches (3.11)

**Most common cause: Missing .env file or wrong WSGI configuration!**
