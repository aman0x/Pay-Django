from django.db import models
from userApp.models import CustomUser

USER_ACCOUNT_TYPE = (
    ("INDIVIDUAL", "Individual"),
    ("BUSINESS", "Business")
)

BANK_ACCOUNT_TYPE = (
    ("SAVINGS", "Savings"),
    ("CURRENT", "Current")
)

class BankAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    ifsc_code = models.CharField(max_length=200, blank=True, null=True)
    user_account_type = models.CharField(max_length=20, choices=USER_ACCOUNT_TYPE, default="INDIVIDUAL")
    bank_account_type = models.CharField(max_length=20, choices=BANK_ACCOUNT_TYPE, default="SAVINGS")
    pan_no = models.CharField(max_length=200, blank=True, null=True)
    gstin_no = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return f"{self.account_name} {self.account_number}"

class Beneficiary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    ifsc_code = models.CharField(max_length=200, blank=True, null=True)
    bank_account_type = models.CharField(max_length=20, choices=BANK_ACCOUNT_TYPE, default="SAVINGS")
    pan_no = models.CharField(max_length=200, blank=True, null=True)
    gstin_no = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.account_name} {self.account_number}"