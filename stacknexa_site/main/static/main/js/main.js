// ==========================================
// StackNexa Solutions - Main JavaScript
// ==========================================

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================
    // Navigation
    // ==========================================
    
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Mobile menu toggle
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
        
        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            });
        });
    }
    
    // ==========================================
    // Smooth Scrolling
    // ==========================================
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // ==========================================
    // Counter Animation for Stats
    // ==========================================
    
    const statNumbers = document.querySelectorAll('.stat-number');
    
    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-count'));
        const duration = 2000; // 2 seconds
        const step = target / (duration / 16); // 60fps
        let current = 0;
        
        const timer = setInterval(function() {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            
            // Add + or % suffix based on content
            const suffix = element.textContent.includes('%') ? '%' : '+';
            element.textContent = Math.floor(current) + (suffix === '+' ? '+' : '%');
        }, 16);
    }
    
    // Intersection Observer for counter animation
    if (statNumbers.length > 0) {
        const observerOptions = {
            threshold: 0.5,
            rootMargin: '0px'
        };
        
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    animateCounter(entry.target);
                }
            });
        }, observerOptions);
        
        statNumbers.forEach(stat => observer.observe(stat));
    }
    
    // ==========================================
    // AI Chatbot
    // ==========================================
    
    const chatToggle = document.getElementById('chatToggle');
    const chatPopup = document.getElementById('chatPopup');
    const chatInput = document.getElementById('chatInput');
    const chatSend = document.getElementById('chatSend');
    const chatMessages = document.getElementById('chatMessages');
    
    // Toggle chat popup
    if (chatToggle) {
        chatToggle.addEventListener('click', function() {
            chatPopup.classList.toggle('active');
            this.classList.toggle('active');
            
            // Focus input when opening
            if (chatPopup.classList.contains('active')) {
                setTimeout(() => chatInput.focus(), 300);
            }
        });
    }
    
    // Send message function
    async function sendMessage() {
        const message = chatInput.value.trim();
        
        if (!message) return;
        
        // Add user message to chat
        addMessage(message, 'user');
        chatInput.value = '';
        
        // Show typing indicator
        const typingIndicator = addTypingIndicator();
        
        try {
            // Send to backend API
            const response = await fetch('/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    name: '' // Optional: can add name input
                })
            });
            
            const data = await response.json();
            
            // Remove typing indicator
            typingIndicator.remove();
            
            if (data.success) {
                // Add bot response
                addMessage(data.response, 'bot');
            } else {
                addMessage('Sorry, I encountered an error. Please try again or contact us directly.', 'bot');
            }
        } catch (error) {
            console.error('Chat error:', error);
            typingIndicator.remove();
            addMessage('Sorry, I\'m having trouble connecting. Please try again later or contact us via WhatsApp.', 'bot');
        }
    }
    
    // Add message to chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${sender}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const p = document.createElement('p');
        p.textContent = text;
        
        contentDiv.appendChild(p);
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return messageDiv;
    }
    
    // Add typing indicator
    function addTypingIndicator() {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'chat-message bot-message';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
        
        contentDiv.appendChild(indicator);
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return messageDiv;
    }
    
    // Send button click
    if (chatSend) {
        chatSend.addEventListener('click', sendMessage);
    }
    
    // Enter key to send
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
    
    // ==========================================
    // Contact Form Enhancement
    // ==========================================
    
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Form will submit normally to Django backend
            // Add any client-side validation here if needed
            
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = `
                    <span>Sending...</span>
                    <svg class="animate-spin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10" opacity="0.25"></circle>
                        <path d="M4 12a8 8 0 018-8" opacity="0.75"></path>
                    </svg>
                `;
            }
        });
    }
    
    // ==========================================
    // Scroll Animations
    // ==========================================
    
    // Fade in elements on scroll
    const fadeElements = document.querySelectorAll('.service-card, .portfolio-card, .why-card, .value-item');
    
    if (fadeElements.length > 0) {
        const fadeObserver = new IntersectionObserver(function(entries) {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.animation = `fadeInUp 0.6s ease forwards`;
                    }, index * 100);
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });
        
        fadeElements.forEach(element => {
            element.style.opacity = '0';
            fadeObserver.observe(element);
        });
    }
    
    // ==========================================
    // Auto-hide messages after 5 seconds
    // ==========================================
    
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease forwards';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });
    
    // ==========================================
    // Prevent chat from closing when clicking inside
    // ==========================================
    
    if (chatPopup) {
        chatPopup.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
    
    // Close chat when clicking outside
    document.addEventListener('click', function(e) {
        if (chatPopup && chatPopup.classList.contains('active')) {
            if (!chatPopup.contains(e.target) && !chatToggle.contains(e.target)) {
                chatPopup.classList.remove('active');
                chatToggle.classList.remove('active');
            }
        }
    });
    
    // ==========================================
    // Performance Optimization: Lazy Loading
    // ==========================================
    
    // Add lazy loading to images if needed
    const images = document.querySelectorAll('img[data-src]');
    if (images.length > 0 && 'IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    // ==========================================
    // Console Welcome Message
    // ==========================================
    
    console.log('%c🚀 StackNexaSolutions', 'color: #667eea; font-size: 24px; font-weight: bold;');
    console.log('%cEmpowering Your Digital Success', 'color: #a0aec0; font-size: 14px;');
    console.log('%cWebsite built with Django, React principles, and modern web technologies', 'color: #64748b; font-size: 12px;');
    
});

// ==========================================
// Additional slideOutRight animation for messages
// ==========================================

const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutRight {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100px);
        }
    }
    
    .animate-spin {
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
`;
document.head.appendChild(style);
