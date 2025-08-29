# Travel Booking (Django)

## Quick Start
- Create and activate venv, then pip install -r requirements.txt
- Copy .env.example to .env and set values
- Run: python manage.py migrate && python manage.py runserver

## Features
- User registration/login/logout with profile update
- List and filter travel options by type/source/destination/date
- Book with seat validation and cancellation
- MySQL-ready via env; SQLite fallback
- Responsive templates with Bootstrap
- Unit tests for booking and filters

## Deployment
- For PythonAnywhere: set WSGI app to travel_booking.wsgi, collectstatic, configure virtualenv and env vars
- For AWS: use Gunicorn + Nginx, set DEBUG=False, ALLOWED_HOSTS, and serve static via WhiteNoise/CloudFront

## Setup Instructions

### 1. Environment Setup
```bash
git clone <repository-url>
cd travel
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Database Configuration
Copy `.env.example` to `.env` and configure your database settings:
- For MySQL: Set `USE_SQLITE=False` and configure DB_* variables
- For SQLite (development): Set `USE_SQLITE=True`

### 3. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

## Project Structure

### Apps Overview
- **accounts**: User authentication, registration, and profile management
- **trips**: Travel option listings and filtering
- **bookings**: Booking creation, management, and cancellation

### Key Features
- **Authentication**: Complete user registration/login/logout flow
- **Profile Management**: Users can update their profile information
- **Travel Search**: Filter trips by type, source, destination, and date
- **Booking System**: Book trips with seat validation and inventory management
- **Responsive Design**: Bootstrap-based UI with custom styling

### Technologies Used
- Django 5.0.6
- Bootstrap 5.3.3
- django-crispy-forms for form rendering
- MySQL/SQLite database support
- WhiteNoise for static file serving
- Gunicorn for production deployment

## Testing
Run the test suite:
```bash
python manage.py test
```

## Development Notes
- Uses custom CSS with #00d184 primary color and gradient effects
- Implements proper database transactions for booking operations
- Includes seat validation to prevent overbooking
- All templates extend a responsive base template
- Admin interface configured for easy data management
