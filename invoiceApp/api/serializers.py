from rest_framework import serializers
from invoiceApp.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields= "__all__"
        
class InvoiceSentDashboardSerializer(serializers.Serializer):
    all_invoices = serializers.IntegerField(read_only=True)
    successful = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    today_successful = serializers.IntegerField(read_only=True)
    today_in_progress = serializers.IntegerField(read_only=True)
    today_failed = serializers.IntegerField(read_only=True)
    today_refunded = serializers.IntegerField(read_only=True)
    
class InvoiceReceivedDashboardSerializer(serializers.Serializer):
    all_invoices = serializers.IntegerField(read_only=True)
    successful = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    today_successful = serializers.IntegerField(read_only=True)
    today_in_progress = serializers.IntegerField(read_only=True)
    today_failed = serializers.IntegerField(read_only=True)
    today_refunded = serializers.IntegerField(read_only=True)
    
class InvoiceAllInvoiceSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    recipient = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    account_type = serializers.CharField(read_only=True)
    transaction_id = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.FloatField(read_only=True)
    
class InvoiceDetailsSerializer(serializers.Serializer):
    status = serializers.CharField(read_only=True)
    invoice_title = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    invoice_id = serializers.CharField(read_only=True)
    particulars = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    price_per_quantity = serializers.FloatField(read_only=True)
    amount = serializers.FloatField(read_only=True)
    gst = serializers.IntegerField(read_only=True)
    subtotal = serializers.FloatField(read_only=True)
    name = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    account_number = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    bank_branch = serializers.CharField(read_only=True)    
    ifsc_code = serializers.CharField(read_only=True)
    total_amount = serializers.FloatField(read_only=True)
    
class InvoiceNewInvoicesSerializer(serializers.Serializer):
    invoice_title = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    invoice_id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    bank_branch = serializers.CharField(read_only=True)    
    ifsc_code = serializers.CharField(read_only=True)
    total_amount = serializers.FloatField(read_only=True)    