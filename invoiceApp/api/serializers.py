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