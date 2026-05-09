# 🏗️ System Architecture - StackNexaSolutions

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FRONTEND (Client Side)                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────┐│
│  │   Home   │  │  About   │  │ Services │  │Portfolio │  │Contact││
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  └───────┘│
│       │             │              │              │            │     │
│       └─────────────┴──────────────┴──────────────┴────────────┘    │
│                              │                                       │
│                    ┌─────────┴─────────┐                            │
│                    │                   │                            │
│              ┌─────▼─────┐      ┌─────▼─────┐                      │
│              │   Chat    │      │  WhatsApp │                      │
│              │  Widget   │      │  Button   │                      │
│              └─────┬─────┘      └───────────┘                      │
│                    │                                                 │
└────────────────────┼─────────────────────────────────────────────────┘
                     │
                     │ AJAX/Fetch
                     │
┌────────────────────▼─────────────────────────────────────────────────┐
│                      BACKEND (Django Server)                         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      URL Router                              │   │
│  │  / → home_view                                               │   │
│  │  /about/ → about_view                                        │   │
│  │  /services/ → services_view                                  │   │
│  │  /portfolio/ → portfolio_view                                │   │
│  │  /contact/ → contact_view                                    │   │
│  │  /api/chat/ → chat_api                                       │   │
│  └─────┬───────────────────────────────────────────────────────┘   │
│        │                                                             │
│  ┌─────▼──────────────────────────────────────────────────┐        │
│  │                    Views Layer                           │        │
│  │  ┌────────────┐  ┌────────────┐  ┌─────────────┐       │        │
│  │  │Page Views  │  │Contact     │  │Chat API     │       │        │
│  │  │(Templates) │  │Form Handler│  │(OpenAI)     │       │        │
│  │  └─────┬──────┘  └─────┬──────┘  └─────┬───────┘       │        │
│  └────────┼───────────────┼───────────────┼───────────────┘        │
│           │               │               │                          │
│  ┌────────▼───────────────▼───────────────▼───────────────┐        │
│  │                   Models Layer                           │        │
│  │  ┌──────────────────┐    ┌──────────────────────┐       │        │
│  │  │  ChatMessage     │    │ ContactSubmission    │       │        │
│  │  ├──────────────────┤    ├──────────────────────┤       │        │
│  │  │ - name           │    │ - name               │       │        │
│  │  │ - message        │    │ - email              │       │        │
│  │  │ - response       │    │ - message            │       │        │
│  │  │ - timestamp      │    │ - submitted_at       │       │        │
│  │  │ - is_user        │    │ - is_read            │       │        │
│  │  └────────┬─────────┘    └────────┬─────────────┘       │        │
│  └───────────┼──────────────────────┼─────────────────────┘        │
│              │                      │                                │
└──────────────┼──────────────────────┼────────────────────────────────┘
               │                      │
               │                      │
┌──────────────▼──────────────────────▼────────────────────────────────┐
│                         Database Layer                                │
├───────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    SQLite / PostgreSQL                        │   │
│  │                                                               │   │
│  │  Tables:                                                      │   │
│  │  ┌─────────────────┐     ┌──────────────────────┐           │   │
│  │  │ main_chatmessage│     │main_contactsubmission│           │   │
│  │  └─────────────────┘     └──────────────────────┘           │   │
│  │  ┌─────────────────┐     ┌──────────────────────┐           │   │
│  │  │  auth_user      │     │  django_session      │           │   │
│  │  └─────────────────┘     └──────────────────────┘           │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────────┐
│                      External Services                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌───────────────────┐          ┌──────────────────┐                  │
│  │  OpenAI API       │          │   WhatsApp       │                  │
│  │  (GPT-3.5 Turbo)  │          │   (wa.me)        │                  │
│  │                   │          │                  │                  │
│  │  - Chat API       │          │  - Direct Link   │                  │
│  │  - Completions    │          │  - Pre-filled    │                  │
│  │  - Temperature    │          │    Message       │                  │
│  └───────────────────┘          └──────────────────┘                  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────────┐
│                      Static Files Structure                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  main/static/main/                                                      │
│  ├── css/                                                               │
│  │   └── styles.css        (2,500+ lines - all styling)                │
│  │                                                                       │
│  ├── js/                                                                │
│  │   └── main.js           (400+ lines - interactivity)                │
│  │                                                                       │
│  └── images/                                                            │
│      └── (placeholder for your images)                                 │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────────┐
│                      Request Flow Example                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  USER SENDS CHAT MESSAGE:                                              │
│                                                                          │
│  1. User types message → JavaScript captures input                     │
│  2. JavaScript sends AJAX POST to /api/chat/                           │
│  3. Django receives request → chat_api view                            │
│  4. View saves message to ChatMessage model                            │
│  5. View calls OpenAI API with system prompt                           │
│  6. OpenAI returns AI response                                         │
│  7. View saves response to database                                    │
│  8. View returns JSON response to frontend                             │
│  9. JavaScript displays message in chat UI                             │
│  10. User sees AI response                                             │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────────┐
│                      Deployment Architecture                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PRODUCTION SETUP:                                                      │
│                                                                          │
│  ┌──────────────┐                                                       │
│  │   Browser    │                                                       │
│  └──────┬───────┘                                                       │
│         │ HTTPS                                                         │
│  ┌──────▼───────────────────────────────────────┐                     │
│  │         Load Balancer / CDN                   │                     │
│  │         (Cloudflare, AWS CloudFront)          │                     │
│  └──────┬───────────────────────────────────────┘                     │
│         │                                                               │
│  ┌──────▼───────────────────────────────────────┐                     │
│  │         Web Server                            │                     │
│  │         (Gunicorn + Nginx)                    │                     │
│  └──────┬───────────────────────────────────────┘                     │
│         │                                                               │
│  ┌──────▼───────────────────────────────────────┐                     │
│  │         Django Application                    │                     │
│  │         (Your StackNexaSolutions Code)        │                     │
│  └──────┬───────────────────────────────────────┘                     │
│         │                                                               │
│  ┌──────▼───────────────────────────────────────┐                     │
│  │         Database Server                       │                     │
│  │         (PostgreSQL / MySQL)                  │                     │
│  └───────────────────────────────────────────────┘                     │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘


┌────────────────────────────────────────────────────────────────────────┐
│                      Admin Panel Structure                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Django Admin (/admin/)                                                 │
│  │                                                                       │
│  ├── Authentication and Authorization                                  │
│  │   ├── Users                                                          │
│  │   └── Groups                                                         │
│  │                                                                       │
│  ├── Main                                                               │
│  │   ├── Chat Messages                                                  │
│  │   │   ├── View all conversations                                    │
│  │   │   ├── Search by name/message                                    │
│  │   │   ├── Filter by date/user                                       │
│  │   │   └── Export data                                               │
│  │   │                                                                   │
│  │   └── Contact Submissions                                           │
│  │       ├── View all submissions                                      │
│  │       ├── Mark as read/unread                                       │
│  │       ├── Search by name/email                                      │
│  │       └── Filter by date/status                                     │
│  │                                                                       │
│  └── Sessions                                                           │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘


KEY COMPONENTS:
===============

Frontend:
- 5 HTML pages (Django templates)
- Premium CSS (2,500+ lines)
- Vanilla JavaScript (400+ lines)
- Responsive design
- Smooth animations

Backend:
- Django 6.0.4 framework
- 2 database models
- RESTful API endpoint
- Admin interface
- Form processing

External:
- OpenAI GPT-3.5 API
- WhatsApp integration
- Email ready (optional)

Security:
- CSRF protection
- Environment variables
- SQL injection prevention
- XSS protection
- Secure sessions

Performance:
- Static file serving
- Database optimization
- Lazy loading ready
- CDN ready
- Caching ready
```

---

**Architecture designed for:**
- ✅ Scalability
- ✅ Maintainability
- ✅ Security
- ✅ Performance
- ✅ Extensibility
