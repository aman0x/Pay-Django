from django.db import models
from userApp.models import CustomUser
from accountApp.models import Beneficiary

PAYMENT_TYPE = (
    ("VENDOR_PAYMENT", "Vendor_Payment"),
    ("INDIVIDUAL", "Individual")
)

class Invoice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE, default="INDIVIDUAL")
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return f"{self.user} {self.receiver} {self.amount}"