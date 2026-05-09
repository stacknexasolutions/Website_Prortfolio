# 🚀 QUICK START GUIDE - StackNexaSolutions Website

## ⚡ Get Started in 3 Minutes!

### Step 1: Install Dependencies
```bash
cd stacknexa_site
pip install -r requirements.txt
```

### Step 2: Setup Environment (IMPORTANT!)
```bash
# Create .env file from template
cp .env.example .env

# Edit .env and add your OpenAI API key
# On Windows: notepad .env
# On Mac/Linux: nano .env
```

**Add your OpenAI API key:**
```
OPENAI_API_KEY=sk-your-actual-key-here
```

Get your key from: https://platform.openai.com/api-keys

### Step 3: Setup Database
```bash
python manage.py migrate
```

### Step 4: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### Step 5: Run the Server
```bash
python manage.py runserver
```

### Step 6: Open in Browser
Go to: **http://127.0.0.1:8000/**

---

## ✅ What You Get

✨ **5 Beautiful Pages:**
- Home (Hero + Services Preview)
- About (Company Info)
- Services (Detailed Services)
- Portfolio (Project Showcase)
- Contact (Form + Info)

🤖 **AI Chatbot:**
- Click chat icon (bottom-right)
- Ask about services
- Auto-saves to database

💬 **WhatsApp Integration:**
- Direct chat button
- Pre-filled message

📊 **Admin Panel:**
- View chat messages
- Manage contact submissions
- Go to: http://127.0.0.1:8000/admin/

---

## 🎨 Customization Quick Tips

### Change Colors
Edit: `main/static/main/css/styles.css`
```css
:root {
    --color-primary: #667eea;
}
```

### Update WhatsApp Number
Find and replace in `main/templates/main/base.html`:
```
wa.me/919876543210
```

### Modify Company Info
Edit templates in: `main/templates/main/`

### Customize Chatbot
Edit: `main/views.py` (chat_api function)

---

## 🐛 Common Issues

**Problem: "OpenAI API key missing"**
**Solution:** Add OPENAI_API_KEY to .env file

**Problem: "Static files not loading"**
**Solution:** Run `python manage.py collectstatic`

**Problem: "Port 8000 in use"**
**Solution:** Run `python manage.py runserver 8080`

---

## 📚 Full Documentation

See **README.md** for complete documentation including:
- Detailed setup instructions
- Production deployment guide
- API documentation
- Security best practices

---

## 🎯 Next Steps

1. ✅ Test all pages
2. ✅ Try the chatbot
3. ✅ Submit contact form
4. ✅ Check admin panel
5. ✅ Customize content
6. ✅ Update WhatsApp number
7. ✅ Add real projects to portfolio
8. ✅ Deploy to production!

---

**Need Help?** Check README.md or Django docs: https://docs.djangoproject.com/

**Made with ❤️ for StackNexaSolutions**
