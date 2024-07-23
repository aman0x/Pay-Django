from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
import string
import random
from userApp.models import Beneficiary

User = get_user_model()

def generate_unique_invoice_number():
    while True:
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=13))
        invoice_number = letters + numbers
        if not Invoice.objects.filter(invoice_number=invoice_number).exists():
            return invoice_number

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    user = models.ForeignKey(User, related_name='invoices', on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, related_name='received_invoices', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    services = models.ManyToManyField(Service)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=settings.INVOICE_STATUSES, default='draft')
    invoice_number = models.CharField(max_length=15, unique=True, blank=False, default='')

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = generate_unique_invoice_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.beneficiary.name}"
