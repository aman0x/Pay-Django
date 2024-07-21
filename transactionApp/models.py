from django.db import models
from django.conf import settings
from invoiceApp.models import Service
from userApp.models import BankAccount
from cardApp.models import Card

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('card', 'Card'),
        ('bank', 'Bank'),
    )

    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    receivable_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_transactions', on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    card = models.ForeignKey(Card, null=True, blank=True, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.receivable_user.username} - {self.transaction_amount}"
