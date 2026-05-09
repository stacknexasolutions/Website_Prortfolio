# 🚀 Deployment Guide - StackNexaSolutions

Complete guide to deploy your website to production on various platforms.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:

- ✅ Tested locally and everything works
- ✅ Added your OpenAI API key to environment
- ✅ Updated WhatsApp number in templates
- ✅ Customized content (company info, projects)
- ✅ Created admin user account
- ✅ Collected static files
- ✅ Set DEBUG=False in production settings
- ✅ Updated ALLOWED_HOSTS with your domain

---

## 🌐 Deployment Options

### Option 1: Heroku (Easiest - Recommended for Beginners)
### Option 2: DigitalOcean (More Control)
### Option 3: AWS EC2 (Enterprise)
### Option 4: PythonAnywhere (Quick & Free)
### Option 5: Vercel (Modern)

---

## 1️⃣ Heroku Deployment (RECOMMENDED)

Heroku is the easiest platform for Django deployment with free tier available.

### Prerequisites
- Heroku account (free): https://signup.heroku.com/
- Heroku CLI installed: https://devcenter.heroku.com/articles/heroku-cli

### Step-by-Step Instructions

#### 1. Install Additional Dependencies

Add to `requirements.txt`:
```
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
dj-database-url==2.1.0
```

Install them:
```bash
pip install gunicorn whitenoise psycopg2-binary dj-database-url
```

#### 2. Update settings.py

Add at the top (after imports):
```python
import dj_database_url

# Production settings
if not DEBUG:
    # WhiteNoise for static files
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Database
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
```

#### 3. Create Heroku App

```bash
# Login to Heroku
heroku login

# Create new app (replace 'your-app-name')
heroku create your-app-name

# Add Python buildpack
heroku buildpacks:add heroku/python
```

#### 4. Set Environment Variables

```bash
heroku config:set OPENAI_API_KEY=your-openai-key-here
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

#### 5. Add PostgreSQL Database

```bash
heroku addons:create heroku-postgresql:mini
```

#### 6. Deploy

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Deploy to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create admin user
heroku run python manage.py createsuperuser

# Open your site
heroku open
```

#### 7. View Logs (if issues)

```bash
heroku logs --tail
```

### Your site is now live! 🎉

URL: `https://your-app-name.herokuapp.com`

---

## 2️⃣ DigitalOcean Deployment

More control, better performance, costs $4-5/month.

### Prerequisites
- DigitalOcean account
- Basic Linux knowledge

### Quick Setup

#### 1. Create Droplet
- Choose Ubuntu 22.04 LTS
- Select $4/month plan
- Add SSH key

#### 2. Connect to Server
```bash
ssh root@your-server-ip
```

#### 3. Install Dependencies
```bash
# Update system
apt update && apt upgrade -y

# Install Python and dependencies
apt install python3-pip python3-venv nginx supervisor -y

# Install PostgreSQL
apt install postgresql postgresql-contrib -y
```

#### 4. Setup Project
```bash
# Create user
adduser stacknexa
usermod -aG sudo stacknexa
su - stacknexa

# Clone or upload your project
git clone your-repo-url
cd stacknexa_site

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install gunicorn
```

#### 5. Setup PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE stacknexa_db;
CREATE USER stacknexa_user WITH PASSWORD 'strong-password';
GRANT ALL PRIVILEGES ON DATABASE stacknexa_db TO stacknexa_user;
\q
```

#### 6. Configure Environment
```bash
# Create .env file
nano .env

# Add:
OPENAI_API_KEY=your-key
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgres://stacknexa_user:strong-password@localhost/stacknexa_db
```

#### 7. Run Migrations
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

#### 8. Setup Gunicorn
```bash
# Create systemd service
sudo nano /etc/systemd/system/stacknexa.service

# Add:
[Unit]
Description=StackNexa Gunicorn
After=network.target

[Service]
User=stacknexa
Group=www-data
WorkingDirectory=/home/stacknexa/stacknexa_site
Environment="PATH=/home/stacknexa/stacknexa_site/venv/bin"
ExecStart=/home/stacknexa/stacknexa_site/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/stacknexa/stacknexa_site/stacknexa.sock \
          stacknexa_site.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start stacknexa
sudo systemctl enable stacknexa
```

#### 9. Configure Nginx
```bash
sudo nano /etc/nginx/sites-available/stacknexa

# Add:
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/stacknexa/stacknexa_site;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/stacknexa/stacknexa_site/stacknexa.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/stacknexa /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### 10. Setup SSL (Free with Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

### Your site is now live with HTTPS! 🎉

---

## 3️⃣ AWS EC2 Deployment

Enterprise-grade deployment.

### Quick Steps

1. **Launch EC2 Instance**
   - Choose Ubuntu 22.04
   - t2.micro for free tier
   - Configure security groups (HTTP, HTTPS, SSH)

2. **Follow DigitalOcean steps** (same process)

3. **Use RDS for Database** (optional)
   - Create PostgreSQL RDS instance
   - Update DATABASE_URL in .env

4. **Use S3 for Static Files** (optional)
   - Install django-storages
   - Configure AWS credentials
   - Update STATIC_URL

---

## 4️⃣ PythonAnywhere (Free Option)

Good for testing/small projects.

### Steps

1. **Sign up**: https://www.pythonanywhere.com/
2. **Upload files** via Files tab
3. **Install requirements** in Bash console:
   ```bash
   pip install --user -r requirements.txt
   ```
4. **Configure Web App**
   - Add new web app
   - Choose Django
   - Point to your project
   - Set environment variables in .env
5. **Run migrations** in console:
   ```bash
   python manage.py migrate
   ```
6. **Reload** web app

Limitations: No HTTPS on free tier, limited resources

---

## 5️⃣ Vercel Deployment

Modern, fast, with serverless functions.

### Prerequisites
- Vercel account: https://vercel.com/signup
- Vercel CLI: `npm install -g vercel`

### Setup

1. **Install Vercel adapter**
   ```bash
   pip install django-vercel
   ```

2. **Create vercel.json**
   ```json
   {
     "builds": [
       {
         "src": "stacknexa_site/wsgi.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "stacknexa_site/wsgi.py"
       }
     ]
   }
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Set environment variables** in Vercel dashboard

Note: May need additional configuration for static files

---

## 🔒 Security Best Practices

### 1. Environment Variables
Never commit `.env` to git:
```bash
echo ".env" >> .gitignore
```

### 2. Strong Secret Key
Generate new:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 3. HTTPS Only
In settings.py (production):
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 4. ALLOWED_HOSTS
Only add your domains:
```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### 5. Database Backups
Set up regular backups:
- Heroku: Automatic with PostgreSQL
- DigitalOcean: Use DigitalOcean Backups
- AWS: RDS automated backups

---

## 📊 Post-Deployment

### 1. Test Everything
- ✅ All pages load correctly
- ✅ Chatbot works
- ✅ Contact form submits
- ✅ Admin panel accessible
- ✅ WhatsApp button works
- ✅ Static files load

### 2. Setup Monitoring
- Use Sentry for error tracking
- Setup uptime monitoring (UptimeRobot)
- Configure email alerts

### 3. Performance Optimization
- Enable Gzip compression
- Use CDN for static files
- Optimize database queries
- Cache frequently accessed data

### 4. SEO
- Submit sitemap to Google
- Add Google Analytics
- Configure meta tags
- Setup Google Search Console

---

## 🐛 Common Deployment Issues

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Database Connection Error
Check DATABASE_URL in environment variables

### 500 Internal Server Error
Check logs:
```bash
heroku logs --tail  # Heroku
sudo journalctl -u stacknexa  # DigitalOcean/AWS
```

### WhiteNoise Not Working
Ensure middleware is in correct position in settings.py

---

## 📞 Getting Help

- Django Docs: https://docs.djangoproject.com/
- Heroku Docs: https://devcenter.heroku.com/
- DigitalOcean Tutorials: https://www.digitalocean.com/community/tutorials

---

## 🎯 Recommended Deployment Path

**For Beginners**: Start with Heroku
**For Learning**: Try DigitalOcean
**For Production**: Use AWS or DigitalOcean
**For Quick Demo**: Use PythonAnywhere

---

**🎉 Congratulations on deploying your site!**

Your StackNexaSolutions website is now live and accessible to the world!
