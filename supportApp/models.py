# models.py
from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    TOPIC_CHOICES = [
        ('general', 'General'),
        ('payment', 'Payment'),
        ('kyc', 'KYC'),
        ('account', 'Account'),
        ('transactions', 'Transactions'),
        ('Cards', 'cards'),
        ('other', 'Other'),
    ]

    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    heading = models.CharField(max_length=255)
    subtext = models.TextField()

    def __str__(self):
        return self.heading
