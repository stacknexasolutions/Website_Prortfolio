from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import ChatMessage, ContactSubmission
import json
import os
from openai import OpenAI

def home(request):
    """Home page view"""
    return render(request, 'main/home.html')

def about(request):
    """About page view"""
    return render(request, 'main/about.html')

def services(request):
    """Services page view"""
    return render(request, 'main/services.html')

def portfolio(request):
    """Portfolio page view"""
    return render(request, 'main/portfolio.html')

def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to database
        ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'main/contact.html')

@csrf_exempt
def chat_api(request):
    """AI Chatbot API endpoint"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            user_name = data.get('name', '')
            
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)
            
            # Save user message to database
            chat_msg = ChatMessage.objects.create(
                name=user_name,
                message=user_message,
                is_user=True
            )
            
            # Create system prompt for the chatbot
            system_prompt = """You are an AI assistant for StackNexaSolutions, a premium freelance tech company. 
            
Company Services:
- Cloud Solutions (AWS, Azure, GCP)
- Full Stack Development (React, Django, Node.js, etc.)
- Data Analysis & Visualization
- Data Science & Machine Learning
- Dashboard & Analytics Solutions

Your role:
1. Answer questions about our services professionally and concisely
2. Help clients understand our offerings
3. Be friendly, professional, and helpful
4. If someone wants to discuss a project, suggest they contact us via WhatsApp or the contact form
5. Keep responses brief and to the point (2-3 sentences max)

WhatsApp contact: https://wa.me/919876543210 (example - user should update this)

Be conversational but professional. Focus on how we can help solve their problems."""
            
            # Get AI response using OpenAI
            api_key = os.getenv('OPENAI_API_KEY')
            
            if api_key:
                try:
                    # Initialize client only when needed
                    client = OpenAI(api_key=api_key)
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_message}
                        ],
                        max_tokens=150,
                        temperature=0.7
                    )
                    
                    ai_response = response.choices[0].message.content
                    
                    # Save AI response to database
                    chat_msg.response = ai_response
                    chat_msg.save()
                    
                    return JsonResponse({
                        'success': True,
                        'response': ai_response
                    })
                    
                except Exception as openai_error:
                    print(f"OpenAI Error: {openai_error}")
                    # Fall through to fallback response
            
            # Fallback response when API key is missing or OpenAI fails
            fallback_response = "Thank you for your message! I'm here to help you learn about our services. For detailed discussions, please contact us via WhatsApp or the contact form. How can I assist you today?"
            
            chat_msg.response = fallback_response
            chat_msg.save()
            
            return JsonResponse({
                'success': True,
                'response': fallback_response,
                'note': 'Using fallback response (OpenAI API key may be missing or there was an error)'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
