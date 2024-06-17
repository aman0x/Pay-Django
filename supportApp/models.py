from django.db import models
from userApp.models import CustomUser

class Support(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    def __str__(self):
        return f"{self.user} {self.name}"