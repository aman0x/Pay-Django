from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Topic(models.Model):
    name = models.CharField(max_length=100)

class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    data = models.TextField()
    status = models.CharField(max_length=50)
    is_new = models.BooleanField(default=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_common = models.BooleanField(default=False)  # To distinguish common notifications

class UserNotification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
