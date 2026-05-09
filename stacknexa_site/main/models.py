from django.db import models
from django.utils import timezone

class ChatMessage(models.Model):
    """Store chat messages from users and AI responses"""
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_user = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'
    
    def __str__(self):
        return f"{self.name or 'Anonymous'} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class ContactSubmission(models.Model):
    """Store contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.email} ({self.submitted_at.strftime('%Y-%m-%d')})"
