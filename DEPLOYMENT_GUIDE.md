# 🚀 Travel Booking App - Easy Deployment Guide

## 📋 What's Been Fixed for Easy Deployment

✅ **ALLOWED_HOSTS** - Now includes your domain by default  
✅ **Environment Configuration** - Flexible settings for any platform  
✅ **Static Files** - WhiteNoise configured for production  
✅ **Database** - Works with SQLite (default) or MySQL  
✅ **Security Settings** - Production-ready security configurations  

---

## 🔧 Deploy to PythonAnywhere (Recommended)

### Step 1: Upload Your Project
1. **Zip your project folder** (travel)
2. **Go to PythonAnywhere** → **Files** tab
3. **Upload and extract** your project to `/home/YourUsername/`

### Step 2: Create Environment File
1. **In Files tab**, navigate to your project folder
2. **Create new file** called `.env`
3. **Copy content from `deployment_config.txt`:**
   ```
   DEBUG=False
   SECRET_KEY=your-production-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1,deepanshugupta.pythonanywhere.com
   USE_SQLITE=True
   ```
4. **Replace `your-production-secret-key-here`** with a secure secret key

### Step 3: Install Dependencies
1. **Go to Consoles** tab → **Start new Bash console**
2. **Run these commands:**
   ```bash
   cd travel
   pip3.11 install --user -r requirements.txt
   python3.11 manage.py migrate
   python3.11 manage.py collectstatic --noinput
   python3.11 manage.py createsuperuser  # Optional: create admin user
   ```

### Step 4: Configure Web App
1. **Go to Web** tab → **Add a new web app**
2. **Choose Manual configuration** → **Python 3.11**
3. **Set Source code:** `/home/YourUsername/travel`
4. **Set Working directory:** `/home/YourUsername/travel`
5. **Edit WSGI file** and replace content with:
   ```python
   import os
   import sys
   
   path = '/home/YourUsername/travel'  # Replace YourUsername
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

### Step 5: Set Static Files
1. **In Web tab**, set **Static files:**
   - **URL:** `/static/`
   - **Directory:** `/home/YourUsername/travel/staticfiles/`

### Step 6: Reload and Test
1. **Click "Reload"** button
2. **Visit your website:** `https://yourusername.pythonanywhere.com`

---

## 🌐 Deploy to Other Platforms

### Heroku
1. **Add `Procfile`:**
   ```
   web: gunicorn travel_booking.wsgi --log-file -
   ```
2. **Set environment variables** in Heroku dashboard
3. **Deploy using Git**

### DigitalOcean/AWS/VPS
1. **Upload project files**
2. **Create `.env` file** with production settings
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Run migrations:** `python manage.py migrate`
5. **Collect static files:** `python manage.py collectstatic`
6. **Configure web server** (Nginx + Gunicorn)

---

## 🔒 Security Checklist

- [ ] Set strong `SECRET_KEY` in production
- [ ] Set `DEBUG=False` in production
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Use HTTPS in production
- [ ] Create admin user: `python manage.py createsuperuser`
- [ ] Regular database backups

---

## 🐛 Common Issues & Solutions

### "DisallowedHost" Error
**Solution:** Check your `.env` file has correct `ALLOWED_HOSTS`

### Static Files Not Loading
**Solution:** Run `python manage.py collectstatic --noinput`

### Database Errors
**Solution:** Run `python manage.py migrate`

### ImportError
**Solution:** Install requirements: `pip install -r requirements.txt`

---

## 📞 Need Help?

Your project is now **deployment-ready**! If you encounter issues:
1. Check the error logs in your hosting platform
2. Verify environment variables are set correctly
3. Ensure all dependencies are installed

**Your app includes:**
- ✈️ Trip browsing and filtering
- 👤 User accounts and profiles  
- 📅 Booking system
- 🎨 Beautiful, responsive design
- 🔐 Secure authentication

Happy deploying! 🎉
