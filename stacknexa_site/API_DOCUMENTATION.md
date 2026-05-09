# 🔌 API Documentation - StackNexaSolutions

## Chat API Endpoint

The StackNexaSolutions website includes a RESTful API endpoint for the AI chatbot functionality.

---

## Endpoint Details

**URL**: `/api/chat/`

**Method**: `POST`

**Authentication**: None (public endpoint with CSRF exempt)

**Content-Type**: `application/json`

---

## Request Format

### Headers
```
Content-Type: application/json
```

### Body Parameters

| Parameter | Type   | Required | Description                          |
|-----------|--------|----------|--------------------------------------|
| message   | string | Yes      | The user's message/question          |
| name      | string | No       | User's name (optional, for tracking) |

### Example Request

```javascript
// JavaScript Fetch API
const response = await fetch('/api/chat/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        message: "What services do you offer?",
        name: "John Doe"  // optional
    })
});

const data = await response.json();
console.log(data.response);
```

```python
# Python Requests
import requests

response = requests.post(
    'http://127.0.0.1:8000/api/chat/',
    json={
        'message': 'What services do you offer?',
        'name': 'John Doe'  # optional
    }
)

data = response.json()
print(data['response'])
```

```bash
# cURL
curl -X POST http://127.0.0.1:8000/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "What services do you offer?", "name": "John Doe"}'
```

---

## Response Format

### Success Response

**Status Code**: `200 OK`

**Body**:
```json
{
    "success": true,
    "response": "We offer Cloud Solutions, Full Stack Development, Data Science & ML, and Dashboard Analytics. How can we help you?"
}
```

If using fallback mode (no OpenAI API key):
```json
{
    "success": true,
    "response": "Thank you for your message! I'm here to help you learn about our services...",
    "note": "Using fallback response (OpenAI API key may be missing or there was an error)"
}
```

### Error Responses

#### Missing Message
**Status Code**: `400 Bad Request`

```json
{
    "error": "Message is required"
}
```

#### Invalid JSON
**Status Code**: `400 Bad Request`

```json
{
    "error": "Invalid JSON"
}
```

#### Server Error
**Status Code**: `500 Internal Server Error`

```json
{
    "error": "Error message details"
}
```

#### Wrong Method
**Status Code**: `405 Method Not Allowed`

```json
{
    "error": "Only POST requests allowed"
}
```

---

## Response Fields

| Field    | Type    | Description                                      |
|----------|---------|--------------------------------------------------|
| success  | boolean | Indicates if the request was successful         |
| response | string  | The AI-generated response to the user's message  |
| note     | string  | Optional field with additional information       |
| error    | string  | Error message (only present on error responses)  |

---

## Database Storage

All messages sent to this endpoint are automatically saved to the database:

**Model**: `ChatMessage`

**Fields**:
- `name` - User's name (if provided)
- `message` - User's message
- `response` - AI's response
- `timestamp` - When the message was sent
- `is_user` - Boolean (always True for user messages)

**Admin Access**: View all messages at `/admin/main/chatmessage/`

---

## Rate Limiting

Currently, there is no rate limiting implemented. For production use, consider adding:

1. **Django Ratelimit**:
```python
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method='POST')
@csrf_exempt
def chat_api(request):
    # ... existing code
```

2. **Throttling** (Django REST Framework):
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
    }
}
```

---

## AI Response Configuration

The chatbot uses OpenAI's GPT-3.5 Turbo model with these settings:

- **Model**: `gpt-3.5-turbo`
- **Max Tokens**: 150
- **Temperature**: 0.7
- **System Prompt**: Customizable in `views.py`

### Customizing AI Behavior

Edit the `system_prompt` in `main/views.py`:

```python
system_prompt = """You are an AI assistant for StackNexaSolutions...

Your custom instructions here...
"""
```

---

## Integration Examples

### React/Next.js

```javascript
// components/Chatbot.js
import { useState } from 'react';

export default function Chatbot() {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        const response = await fetch('/api/chat/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        
        const data = await response.json();
        
        setMessages([
            ...messages,
            { text: message, isUser: true },
            { text: data.response, isUser: false }
        ]);
        
        setMessage('');
    };

    return (
        <div>
            {messages.map((msg, i) => (
                <div key={i} className={msg.isUser ? 'user' : 'bot'}>
                    {msg.text}
                </div>
            ))}
            <input 
                value={message} 
                onChange={(e) => setMessage(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            />
        </div>
    );
}
```

### Vue.js

```javascript
// ChatWidget.vue
<template>
  <div class="chat">
    <div v-for="msg in messages" :key="msg.id">
      {{ msg.text }}
    </div>
    <input v-model="currentMessage" @keyup.enter="sendMessage" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      currentMessage: ''
    }
  },
  methods: {
    async sendMessage() {
      const response = await fetch('/api/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: this.currentMessage })
      });
      
      const data = await response.json();
      
      this.messages.push(
        { text: this.currentMessage, isUser: true },
        { text: data.response, isUser: false }
      );
      
      this.currentMessage = '';
    }
  }
}
</script>
```

### Mobile App (Flutter)

```dart
// chat_service.dart
import 'package:http/http.dart' as http;
import 'dart:convert';

class ChatService {
  static const String apiUrl = 'https://yoursite.com/api/chat/';
  
  Future<String> sendMessage(String message) async {
    final response = await http.post(
      Uri.parse(apiUrl),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'message': message}),
    );
    
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['response'];
    } else {
      throw Exception('Failed to send message');
    }
  }
}
```

---

## CORS Configuration

For cross-origin requests (if frontend is on different domain):

**Install django-cors-headers**:
```bash
pip install django-cors-headers
```

**settings.py**:
```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

# Allow specific origins
CORS_ALLOWED_ORIGINS = [
    "https://yourfrontend.com",
    "http://localhost:3000",  # React dev server
]

# Or allow all (not recommended for production)
# CORS_ALLOW_ALL_ORIGINS = True
```

---

## Security Considerations

1. **CSRF Protection**: Currently disabled for this endpoint
   - Consider adding token-based auth for production
   
2. **Input Validation**: 
   - Message length is not limited
   - Consider adding max length validation
   
3. **Rate Limiting**: 
   - Add rate limiting to prevent abuse
   
4. **API Key Security**:
   - Never expose OpenAI key in frontend
   - Keep it server-side only
   
5. **Content Filtering**:
   - Add profanity/spam filters if needed
   - Implement user reporting

---

## Testing the API

### Using Postman

1. Create new POST request
2. URL: `http://127.0.0.1:8000/api/chat/`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
```json
{
    "message": "Hello, what can you do?",
    "name": "Test User"
}
```
5. Send and verify response

### Using Python Script

```python
# test_chat.py
import requests

def test_chat(message):
    response = requests.post(
        'http://127.0.0.1:8000/api/chat/',
        json={'message': message}
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

# Test various messages
test_chat("What services do you offer?")
test_chat("Tell me about cloud solutions")
test_chat("How can I contact you?")
```

---

## Future Enhancements

Potential improvements for the API:

1. **Authentication** - Add JWT or token-based auth
2. **Conversation History** - Return previous messages
3. **Typing Indicators** - WebSocket for real-time status
4. **File Upload** - Allow image/document analysis
5. **Multi-language** - Support multiple languages
6. **Analytics** - Track common questions
7. **Sentiment Analysis** - Analyze user sentiment
8. **Auto-tagging** - Categorize conversations

---

## Support

For API issues or questions:
- Check Django logs: `python manage.py runserver` output
- Review admin panel: `/admin/main/chatmessage/`
- Enable DEBUG mode temporarily for detailed errors
- Check OpenAI API status: https://status.openai.com/

---

**Last Updated**: 2024
**Version**: 1.0
**Django Version**: 6.0.4
**OpenAI SDK**: 2.31.0
