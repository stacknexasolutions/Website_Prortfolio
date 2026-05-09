# 🚀 StackNexaSolutions - Professional Tech Company Website

A complete, production-ready website for a freelance tech company with **AI-powered chatbot**, premium dark theme, and modern features.

![Premium Dark Theme](https://img.shields.io/badge/Theme-Dark-blueviolet)
![Django](https://img.shields.io/badge/Django-6.0.4-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-blue)

## ✨ Features

### 🎨 Design & UI
- **Premium Dark Theme** with blue, purple, and orange gradients
- **Fully Responsive** - perfect on mobile, tablet, and desktop
- **Smooth Animations** - fade-ins, slides, hover effects
- **Modern Typography** - Urbanist & Space Mono fonts
- **Professional Layout** - startup-style premium design

### 📄 Pages
1. **Home** - Hero section, services preview, stats, CTA
2. **About** - Company info, mission, vision, why choose us
3. **Services** - Detailed service offerings with visuals
   - Cloud Solutions
   - Full Stack Development
   - Data Analysis
   - Data Science & ML
   - Dashboard & Analytics
4. **Portfolio** - Project showcase with dummy projects
5. **Contact** - Contact form with Django backend

### 🤖 AI Chatbot System
- **Floating Chat Button** - bottom-right corner
- **OpenAI GPT Integration** - intelligent responses
- **Auto-reply** - answers questions about services
- **Database Storage** - all messages saved to Django database
- **Fallback Response** - works even without OpenAI API key
- **Modern UI** - WhatsApp-style chat interface

### 💬 Communication Features
- **WhatsApp Button** - direct link with pre-filled message
- **Contact Form** - stores submissions in database
- **Success Messages** - user feedback on form submission

### 🛠️ Technical Features
- **Django Backend** - robust Python framework
- **SQLite Database** - easy setup (upgradeable to PostgreSQL)
- **Environment Variables** - secure API key management
- **Admin Panel** - manage messages and submissions
- **SEO-Friendly** - proper meta tags and structure
- **Fast Loading** - optimized CSS and JS

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key (for chatbot functionality)

## 🚀 Installation & Setup

### 1. Clone or Download the Project

```bash
cd stacknexa_site
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**🔑 Get OpenAI API Key:**
1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy and paste it into `.env`

### 4. Database Setup

Run migrations to create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User (Optional but Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Collect Static Files (Production)

For production deployment:

```bash
python manage.py collectstatic
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

## 🎯 Usage Guide

### Accessing the Website

- **Homepage**: http://127.0.0.1:8000/
- **About**: http://127.0.0.1:8000/about/
- **Services**: http://127.0.0.1:8000/services/
- **Portfolio**: http://127.0.0.1:8000/portfolio/
- **Contact**: http://127.0.0.1:8000/contact/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### Testing the AI Chatbot

1. Click the **chat icon** in the bottom-right corner
2. Type a message like:
   - "What services do you offer?"
   - "Tell me about cloud solutions"
   - "How can you help with data science?"
3. The AI will respond automatically
4. All messages are saved in the database

**Note**: If you don't have an OpenAI API key, the chatbot will use a fallback response system.

### Viewing Chat Messages in Admin

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Click on **Chat Messages** to view all conversations
4. Click on **Contact Submissions** to view contact form entries

### Customizing WhatsApp Number

Update the WhatsApp number in:
1. **templates/main/base.html** - search for `wa.me/919876543210`
2. Replace with your number in format: `countrycode + number` (no spaces)
   - Example: `919876543210` for India
   - Example: `14155551234` for USA

## 🎨 Customization

### Changing Colors

Edit `/main/static/main/css/styles.css`:

```css
:root {
    --color-primary: #667eea;  /* Main brand color */
    --color-secondary: #f093fb; /* Secondary color */
    --color-accent: #4facfe;    /* Accent color */
}
```

### Updating Company Information

Edit templates in `/main/templates/main/`:
- **base.html** - footer, navbar
- **home.html** - hero text, stats
- **about.html** - company story
- **services.html** - service details
- **portfolio.html** - projects

### Modifying Chatbot Behavior

Edit `/main/views.py` in the `chat_api` function:

```python
system_prompt = """You are an AI assistant for StackNexaSolutions...
[Customize the prompt here]
"""
```

## 📊 Project Structure

```
stacknexa_site/
├── main/                      # Main Django app
│   ├── migrations/           # Database migrations
│   ├── static/main/          # Static files
│   │   ├── css/
│   │   │   └── styles.css   # All CSS styles
│   │   └── js/
│   │       └── main.js      # All JavaScript
│   ├── templates/main/       # HTML templates
│   │   ├── base.html        # Base template
│   │   ├── home.html        # Homepage
│   │   ├── about.html       # About page
│   │   ├── services.html    # Services page
│   │   ├── portfolio.html   # Portfolio page
│   │   └── contact.html     # Contact page
│   ├── admin.py             # Admin configuration
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   └── urls.py              # URL routing
├── stacknexa_site/           # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL config
│   └── wsgi.py              # WSGI config
├── .env.example             # Environment variables template
├── requirements.txt         # Python dependencies
├── manage.py                # Django management script
└── README.md                # This file
```

## 🗄️ Database Models

### ChatMessage
- `name` - User name (optional)
- `message` - User's message
- `response` - AI's response
- `timestamp` - When the message was sent
- `is_user` - Boolean flag

### ContactSubmission
- `name` - Contact name
- `email` - Contact email
- `message` - Contact message
- `submitted_at` - Submission timestamp
- `is_read` - Read status flag

## 🔧 API Endpoints

### Chat API
- **URL**: `/api/chat/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "message": "Your message here",
    "name": "Optional name"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "response": "AI response here"
  }
  ```

## 🚀 Production Deployment

### 1. Update Settings

In `stacknexa_site/settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### 2. Use Production Database

Consider upgrading to PostgreSQL:

```bash
pip install psycopg2-binary
```

Update `DATABASES` in settings.py

### 3. Install Production Server

```bash
pip install gunicorn whitenoise
```

### 4. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 5. Run with Gunicorn

```bash
gunicorn stacknexa_site.wsgi:application --bind 0.0.0.0:8000
```

### Deployment Platforms

- **Heroku**: Easy deployment with Postgres support
- **DigitalOcean**: Full control VPS
- **AWS/Azure/GCP**: Scalable cloud hosting
- **PythonAnywhere**: Simple Python hosting
- **Vercel**: (with additional configuration)

## 🔒 Security Notes

1. **Never commit `.env` file** to version control
2. **Change SECRET_KEY** in production
3. **Set DEBUG=False** in production
4. **Use HTTPS** in production
5. **Regularly update dependencies**
6. **Monitor API usage** to avoid unexpected costs

## 🐛 Troubleshooting

### Chatbot Not Working

**Problem**: Chatbot shows fallback message
**Solution**: 
- Check if `OPENAI_API_KEY` is set in `.env`
- Verify API key is valid at OpenAI platform
- Check internet connection
- Review console for errors

### Static Files Not Loading

**Problem**: CSS/JS not applied
**Solution**:
```bash
python manage.py collectstatic
```

### Database Errors

**Problem**: Database-related errors
**Solution**:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Port Already in Use

**Problem**: Port 8000 is busy
**Solution**:
```bash
python manage.py runserver 8080
```

## 📝 License

This project is open source and available for use. Feel free to customize it for your needs.

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Django documentation: https://docs.djangoproject.com/
3. Check OpenAI API docs: https://platform.openai.com/docs/

## 🎯 Next Steps

1. ✅ Install and run the project
2. ✅ Add your OpenAI API key
3. ✅ Test all features
4. ✅ Customize content and branding
5. ✅ Update WhatsApp number
6. ✅ Add real portfolio projects
7. ✅ Deploy to production
8. ✅ Set up custom domain
9. ✅ Monitor and optimize

## 🌟 Credits

Built with:
- Django - Python Web Framework
- OpenAI - GPT-3.5 Turbo
- Modern CSS3 & JavaScript
- Google Fonts (Urbanist, Space Mono)

---

**Made with ❤️ for StackNexaSolutions**

*Empowering Your Digital Success*
