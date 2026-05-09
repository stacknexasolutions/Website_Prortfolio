# 🎨 Customization Guide - StackNexaSolutions

Complete guide to customize your website with code examples.

---

## 📋 Table of Contents

1. [Branding & Colors](#branding--colors)
2. [Content Updates](#content-updates)
3. [WhatsApp Integration](#whatsapp-integration)
4. [Chatbot Customization](#chatbot-customization)
5. [Adding Portfolio Projects](#adding-portfolio-projects)
6. [Contact Form](#contact-form)
7. [Navigation Menu](#navigation-menu)
8. [Footer](#footer)
9. [Advanced Customizations](#advanced-customizations)

---

## 🎨 Branding & Colors

### Change Primary Colors

**File**: `main/static/main/css/styles.css` (Lines 9-16)

```css
:root {
    /* Change these to your brand colors */
    --color-primary: #667eea;     /* Main brand color (purple) */
    --color-secondary: #f093fb;   /* Secondary color (pink) */
    --color-accent: #4facfe;      /* Accent color (blue) */
    --color-success: #10b981;     /* Success (green) */
    --color-warning: #f59e0b;     /* Warning (orange) */
    --color-error: #ef4444;       /* Error (red) */
}
```

**Example**: Change to a green/teal theme:
```css
:root {
    --color-primary: #10b981;     /* Green */
    --color-secondary: #14b8a6;   /* Teal */
    --color-accent: #06b6d4;      /* Cyan */
}
```

### Change Gradients

**File**: `main/static/main/css/styles.css` (Lines 17-22)

```css
/* Custom gradients */
--gradient-primary: linear-gradient(135deg, #FF6B6B 0%, #FFA500 100%);
--gradient-secondary: linear-gradient(135deg, #00D4FF 0%, #0099FF 100%);
```

### Change Background Colors

```css
:root {
    --bg-primary: #0a0e1a;      /* Main background */
    --bg-secondary: #121827;    /* Section backgrounds */
    --bg-tertiary: #1a1f35;     /* Card backgrounds */
}
```

**Light Theme Example**:
```css
:root {
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-tertiary: #f1f5f9;
    --text-primary: #1e293b;
    --text-secondary: #475569;
}
```

### Change Fonts

**File**: `main/templates/main/base.html` (Line 12)

Current fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Urbanist:wght@300;400;600;700;800&display=swap" rel="stylesheet">
```

**Example**: Change to Poppins + Fira Code:
```html
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
```

Then update CSS:
```css
body {
    font-family: 'Poppins', sans-serif;
}

.logo {
    font-family: 'Fira Code', monospace;
}
```

---

## 📝 Content Updates

### Company Name & Tagline

**File**: `main/templates/main/base.html`

**Logo** (Line 25):
```html
<a href="{% url 'home' %}" class="logo">
    <span class="logo-bracket">&lt;</span>
    <span class="logo-text">YourCompany</span>
    <span class="logo-bracket">/&gt;</span>
</a>
```

**Tagline** (home.html, Line 19):
```html
<h1 class="hero-title">
    Your Custom
    <span class="gradient-text">Tagline Here</span>
</h1>
```

### Homepage Hero Section

**File**: `main/templates/main/home.html`

**Hero Badge** (Line 14):
```html
<div class="hero-badge">
    <span class="badge-dot"></span>
    <span>Your Custom Badge Text</span>
</div>
```

**Hero Description** (Line 23):
```html
<p class="hero-subtitle">
    Your company description goes here. Make it compelling and clear.
</p>
```

**CTA Buttons** (Line 28):
```html
<div class="hero-cta">
    <a href="{% url 'contact' %}" class="btn btn-primary">
        Your CTA Text
        <svg>...</svg>
    </a>
</div>
```

### Stats Counter

**File**: `main/templates/main/home.html` (Line 39)

```html
<div class="hero-stats">
    <div class="stat-item">
        <h3 class="stat-number" data-count="100">0</h3>
        <p class="stat-label">Your Metric Here</p>
    </div>
    <!-- Add more stats -->
</div>
```

### About Page Content

**File**: `main/templates/main/about.html`

**Mission** (Line 23):
```html
<div class="highlight-item">
    <h3>🎯 Our Mission</h3>
    <p>Your mission statement here...</p>
</div>
```

**Vision** (Line 27):
```html
<div class="highlight-item">
    <h3>🚀 Our Vision</h3>
    <p>Your vision statement here...</p>
</div>
```

---

## 📱 WhatsApp Integration

### Update WhatsApp Number

**Find and Replace in Files**:
1. `main/templates/main/base.html` (2 locations)
2. `main/views.py` (chatbot prompt)

**Current**: `wa.me/919876543210`

**Format**: `countrycode + number` (no spaces, +, or dashes)

**Examples**:
- USA: `14155551234`
- UK: `447700900123`
- India: `919876543210`

**File**: `main/templates/main/base.html` (Line 154)

```html
<a href="https://wa.me/14155551234?text=Hi%20YourCompany%2C%20I%20want%20to%20discuss%20a%20project." 
   class="whatsapp-btn" 
   target="_blank">
```

### Custom WhatsApp Message

```html
<!-- URL encode your message -->
<a href="https://wa.me/14155551234?text=Hello!%20I%20need%20help%20with%20my%20project.">
```

**Tool**: Use https://meyerweb.com/eric/tools/dencoder/ to encode your message

---

## 🤖 Chatbot Customization

### Modify Chatbot Personality

**File**: `main/views.py` (Line 57)

```python
system_prompt = """You are an AI assistant for [Your Company], a [description].

Company Services:
- Service 1
- Service 2
- Service 3

Your role:
1. [Custom instruction 1]
2. [Custom instruction 2]
3. [Custom instruction 3]

Be [personality trait] and [personality trait].
"""
```

**Example - Friendly & Casual**:
```python
system_prompt = """Hey! You're the super friendly AI helper for TechVentures.

We help startups build awesome products:
- Mobile Apps (iOS & Android)
- Web Platforms
- Cloud Solutions

Your vibe:
1. Keep it casual and fun! Use emojis 😊
2. Talk like you're chatting with a friend
3. If they want to work with us, get them excited and point them to our contact form
4. Keep answers super short - max 2 sentences

Be enthusiastic and helpful!
"""
```

**Example - Professional & Corporate**:
```python
system_prompt = """You are a professional customer service representative for Enterprise Solutions Ltd.

Our Services:
- Enterprise Software Development
- Business Process Automation
- IT Consulting

Guidelines:
1. Maintain formal, professional language
2. Provide detailed, accurate information
3. For project inquiries, collect requirements and suggest scheduling a consultation
4. Always end with "How else may I assist you?"

Represent our brand with professionalism and expertise.
"""
```

### Change Welcome Message

**File**: `main/templates/main/base.html` (Line 171)

```html
<div class="chat-message bot-message">
    <div class="message-content">
        <p>👋 Your custom welcome message here!</p>
    </div>
</div>
```

### Disable Chatbot (Use Fallback Only)

**File**: `main/views.py` (Line 75)

Comment out OpenAI code:
```python
# Skip OpenAI, always use fallback
fallback_response = "Thanks for your message! Please contact us at hello@yourcompany.com"
chat_msg.response = fallback_response
chat_msg.save()
return JsonResponse({'success': True, 'response': fallback_response})
```

---

## 🎯 Adding Portfolio Projects

**File**: `main/templates/main/portfolio.html`

### Add New Project

```html
<div class="portfolio-card">
    <div class="portfolio-image">
        <div class="project-placeholder" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <!-- SVG icon or image -->
            <svg viewBox="0 0 200 200" fill="none" stroke="white" stroke-width="2">
                <!-- Your custom SVG -->
            </svg>
        </div>
    </div>
    <div class="portfolio-content">
        <div class="portfolio-tags">
            <span class="tag">Category</span>
            <span class="tag">Tech</span>
        </div>
        <h3 class="portfolio-title">Project Name</h3>
        <p class="portfolio-description">
            Brief description of what you built and the impact.
        </p>
        <div class="portfolio-tech">
            <span>React</span>
            <span>Django</span>
            <span>PostgreSQL</span>
        </div>
    </div>
</div>
```

### Use Real Images

Replace placeholder with image:
```html
<div class="portfolio-image">
    <img src="{% static 'main/images/project1.jpg' %}" alt="Project Name">
</div>
```

Add CSS for images:
```css
.portfolio-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

---

## 📧 Contact Form

### Add More Fields

**File**: `main/templates/main/contact.html`

Add phone field (after email):
```html
<div class="form-group">
    <label for="phone">Phone Number</label>
    <input type="tel" 
           id="phone" 
           name="phone" 
           class="form-input" 
           placeholder="+1 (555) 123-4567">
</div>
```

**Update Model** (main/models.py):
```python
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)  # Add this
    message = models.TextField()
    # ... rest of model
```

**Update View** (main/views.py):
```python
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # Add this
        message = request.POST.get('message')
        
        ContactSubmission.objects.create(
            name=name,
            email=email,
            phone=phone,  # Add this
            message=message
        )
```

Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Email Notifications

Install email backend:
```bash
pip install django-ses  # For AWS SES
# OR
# Use Gmail SMTP (built-in)
```

**settings.py**:
```python
# Gmail example
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

**views.py** (in contact function):
```python
from django.core.mail import send_mail

# After saving to database
send_mail(
    subject=f'New Contact Form Submission from {name}',
    message=message,
    from_email='noreply@yoursite.com',
    recipient_list=['your-email@company.com'],
    fail_silently=True,
)
```

---

## 🧭 Navigation Menu

### Add New Page

**1. Create View** (main/views.py):
```python
def pricing(request):
    return render(request, 'main/pricing.html')
```

**2. Add URL** (main/urls.py):
```python
path('pricing/', views.pricing, name='pricing'),
```

**3. Create Template** (main/templates/main/pricing.html):
```html
{% extends 'main/base.html' %}
{% block title %}Pricing - StackNexaSolutions{% endblock %}
{% block content %}
<!-- Your pricing content -->
{% endblock %}
```

**4. Add to Navigation** (base.html, Line 28):
```html
<a href="{% url 'pricing' %}" class="nav-link">Pricing</a>
```

### Reorder Menu Items

Just rearrange the nav links in base.html:
```html
<div class="nav-menu" id="navMenu">
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'services' %}">Services</a>
    <a href="{% url 'portfolio' %}">Portfolio</a>
    <a href="{% url 'about' %}">About</a>
    <a href="{% url 'contact' %}">Contact</a>
</div>
```

---

## 🦶 Footer

### Update Contact Info

**File**: `main/templates/main/base.html` (Line 127)

```html
<div class="footer-col">
    <h4 class="footer-subtitle">Contact</h4>
    <ul class="footer-links">
        <li><a href="mailto:hello@yourcompany.com">hello@yourcompany.com</a></li>
        <li><a href="tel:+14155551234">+1 (415) 555-1234</a></li>
        <li><a href="{% url 'contact' %}">Contact Form</a></li>
        <li>123 Main St, San Francisco, CA</li>
    </ul>
</div>
```

### Update Social Links

**File**: `main/templates/main/base.html` (Line 98)

```html
<div class="social-links">
    <a href="https://linkedin.com/company/yourcompany" class="social-link">
        <!-- LinkedIn SVG -->
    </a>
    <a href="https://github.com/yourcompany" class="social-link">
        <!-- GitHub SVG -->
    </a>
    <a href="https://twitter.com/yourcompany" class="social-link">
        <!-- Twitter SVG -->
    </a>
    <!-- Add more: Facebook, Instagram, YouTube, etc. -->
</div>
```

### Add Newsletter Signup

```html
<div class="footer-col">
    <h4 class="footer-subtitle">Newsletter</h4>
    <form method="POST" action="{% url 'newsletter_signup' %}">
        {% csrf_token %}
        <input type="email" name="email" placeholder="Your email" required>
        <button type="submit">Subscribe</button>
    </form>
</div>
```

---

## 🚀 Advanced Customizations

### Add Google Analytics

**File**: `main/templates/main/base.html` (before </head>)

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Add Cookie Consent

```html
<!-- Before </body> -->
<div id="cookie-banner" style="display: none;">
    <p>We use cookies to improve your experience. 
       <a href="/privacy">Learn more</a></p>
    <button onclick="acceptCookies()">Accept</button>
</div>

<script>
function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-banner').style.display = 'none';
}

if (!localStorage.getItem('cookiesAccepted')) {
    document.getElementById('cookie-banner').style.display = 'block';
}
</script>
```

### Add Live Chat (Intercom/Drift)

**File**: `main/templates/main/base.html` (before </body>)

```html
<!-- Intercom -->
<script>
  window.intercomSettings = {
    app_id: "YOUR_APP_ID"
  };
  (function(){var w=window;var ic=w.Intercom;if(typeof ic==="function"){ic('reattach_activator');ic('update',w.intercomSettings);}else{var d=document;var i=function(){i.c(arguments);};i.q=[];i.c=function(args){i.q.push(args);};w.Intercom=i;var l=function(){var s=d.createElement('script');s.type='text/javascript';s.async=true;s.src='https://widget.intercom.io/widget/YOUR_APP_ID';var x=d.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);};if(document.readyState==='complete'){l();}else if(w.attachEvent){w.attachEvent('onload',l);}else{w.addEventListener('load',l,false);}}})();
</script>
```

### Add Blog Section

**1. Create Blog App**:
```bash
python manage.py startapp blog
```

**2. Add to INSTALLED_APPS** (settings.py)

**3. Create Models** (blog/models.py):
```python
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

**4. Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create Views & URLs**

---

## 🎨 Quick Color Schemes

### Midnight Blue
```css
--color-primary: #3b82f6;
--color-secondary: #8b5cf6;
--color-accent: #06b6d4;
```

### Forest Green
```css
--color-primary: #10b981;
--color-secondary: #059669;
--color-accent: #14b8a6;
```

### Sunset Orange
```css
--color-primary: #f97316;
--color-secondary: #fb923c;
--color-accent: #fbbf24;
```

### Royal Purple
```css
--color-primary: #9333ea;
--color-secondary: #a855f7;
--color-accent: #c084fc;
```

---

## 📚 Additional Resources

- Django Templates: https://docs.djangoproject.com/en/5.0/topics/templates/
- CSS Variables: https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties
- Bootstrap: https://getbootstrap.com/ (if you want to add it)
- Tailwind CSS: https://tailwindcss.com/ (alternative styling)

---

**Need more help?** Check the main README.md or Django documentation!
