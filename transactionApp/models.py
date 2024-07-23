from django.db import models
from django.conf import settings
from invoiceApp.models import Service
from userApp.models import BankAccount
from cardApp.models import Card
from userApp.models import Beneficiary

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('card', 'Card'),
        ('bank', 'Bank'),
    )

    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    beneficiary = models.ForeignKey(Beneficiary, related_name='transactions', on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    card = models.ForeignKey(Card, null=True, blank=True, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.beneficiary.name} - {self.transaction_amount}"