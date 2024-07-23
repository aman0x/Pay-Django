from rest_framework import serializers
from invoiceApp.models import Invoice, Service
from django.contrib.auth import get_user_model
from userApp.models import Beneficiary

User = get_user_model()

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    beneficiary = serializers.PrimaryKeyRelatedField(queryset=Beneficiary.objects.all())
    beneficiary_name = serializers.CharField(source='beneficiary.name', read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'user', 'beneficiary', 'beneficiary_name', 'amount', 'tax', 'services', 'created_at', 'status', 'invoice_number']

    def create(self, validated_data):
        user = self.context['request'].user
        beneficiary = validated_data.pop('beneficiary')
        invoice = Invoice.objects.create(user=user, beneficiary=beneficiary, **validated_data)
        return invoice


        
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