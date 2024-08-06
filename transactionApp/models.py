import random
import string
from django.db import models
from invoiceApp.models import Service
from userApp.models import BankAccount
from cardApp.models import Card
from userApp.models import Beneficiary
from django.conf import settings


def generate_transaction_number():
    alpha_part = ''.join(random.choices(string.ascii_uppercase, k=2))
    numeric_part = ''.join(random.choices(string.digits, k=13))
    return alpha_part + numeric_part

class Transaction(models.Model):

    transaction_number = models.CharField(max_length=15, unique=True, editable=False)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    beneficiary = models.ForeignKey(Beneficiary, related_name='transactions', on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    transaction_type = models.CharField(max_length=10, choices=settings.TRANSACTION_TYPES)
    card = models.ForeignKey(Card, null=True, blank=True, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, null=True, blank=True, on_delete=models.CASCADE)
    transaction_status = models.CharField(max_length=10, choices=settings.TRANSACTION_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.transaction_number:
            self.transaction_number = generate_transaction_number()
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_number} - {self.beneficiary.name} - {self.transaction_amount}"
