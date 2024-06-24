from rest_framework import serializers
from paymentApp.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields= "__all__"
        
class PaymentDashboardSerializer(serializers.Serializer):
    all_payments = serializers.IntegerField(read_only=True)
    successful = serializers.IntegerField(read_only=True)
    in_progress = serializers.IntegerField(read_only=True)
    failed = serializers.IntegerField(read_only=True)
    refunded = serializers.IntegerField(read_only=True)
    today_successful = serializers.IntegerField(read_only=True)
    today_in_progress = serializers.IntegerField(read_only=True)
    today_failed = serializers.IntegerField(read_only=True)
    today_refunded = serializers.IntegerField(read_only=True)
    
class PaymentAllPaymentsSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    beneficiary = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    transaction_id = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)
    sum = serializers.FloatField(read_only=True)
    
class PaymentDetailsSerializer(serializers.Serializer):
    status = serializers.CharField(read_only=True)
    payment_title = serializers.CharField(read_only=True)
    transaction_id = serializers.CharField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    phone_number = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    account_number = serializers.CharField(read_only=True)
    bank = serializers.CharField(read_only=True)
    bank_branch = serializers.CharField(read_only=True)
    ifsc_code = serializers.CharField(read_only=True)
    payment_amount = serializers.FloatField(read_only=True)
    convenience_fee = serializers.FloatField(read_only=True)
    tax = serializers.FloatField(read_only=True)
    payment_total_amount = serializers.FloatField(read_only=True)