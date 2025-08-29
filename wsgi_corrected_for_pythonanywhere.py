# This file contains the WSGI configuration required to serve up your
# web application at http://DeepGupta.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# CORRECTED VERSION for your Travel Booking Django project

import os
import sys

# add your project directory to the sys.path
project_home = '/home/DeepGupta/travel'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
# CORRECTED: Your Django project module is 'travel_booking', not 'travel'
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'

# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
