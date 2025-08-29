# DEBUG WSGI file for troubleshooting PythonAnywhere deployment
# Use this temporarily to get more detailed error information

import os
import sys

# add your project directory to the sys.path
project_home = '/home/DeepGupta/travel'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Debug: Print Python path and Django version
print("Python path:", sys.path)
print("Project home:", project_home)

try:
    import django
    print("Django version:", django.get_version())
except ImportError as e:
    print("Django import error:", e)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'

# Debug: Check if settings can be imported
try:
    from django.conf import settings
    print("Settings imported successfully")
    print("DEBUG:", getattr(settings, 'DEBUG', 'Not set'))
    print("ALLOWED_HOSTS:", getattr(settings, 'ALLOWED_HOSTS', 'Not set'))
except Exception as e:
    print("Settings import error:", e)

# serve django via WSGI
try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("WSGI application created successfully")
except Exception as e:
    print("WSGI application error:", e)
    # Create a simple WSGI app that shows the error
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [f'<h1>Error: {str(e)}</h1><p>Check the error logs for more details.</p>'.encode()]
