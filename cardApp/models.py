from django.db import models
from userApp.models import CustomUser
from django.core.exceptions import ValidationError
import re

class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=200, blank=True, null=True)
    card_no = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.CharField(max_length=5, blank=True, null=True)
    cvv_no = models.CharField(max_length=3, blank=True, null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} {self.card_no}"
    
    def clean(self):
        super().clean()
        if self.expiry_date:
            if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', self.expiry_date):
                raise ValidationError("Expiry date must be in MM/YY format.")