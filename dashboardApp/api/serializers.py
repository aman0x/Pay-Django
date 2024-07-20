from rest_framework import serializers

class DashboardQuickSendSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)
    
class DashboardTotalMonthSpendingsSerializer(serializers.Serializer):
    card_number = serializers.CharField(read_only=True)
    card_type = serializers.CharField(read_only=True)
    monthly_income = serializers.DictField(child=serializers.IntegerField())
    monthly_expenses = serializers.DictField(child=serializers.IntegerField())
    incomes = serializers.IntegerField(read_only=True)
    expenses = serializers.IntegerField(read_only=True)

class DashboardMyTemplateSerializer(serializers.Serializer):
    bank_name = serializers.CharField(read_only=True)
    bank_branch_name = serializers.CharField(read_only=True)
    account_holder_name = serializers.CharField(read_only=True)
    ifsc_code = serializers.CharField(read_only=True)
    
class DashboardMyCardSerializer(serializers.Serializer):
    card_holder_name = serializers.CharField(read_only=True)
    card_number = serializers.CharField(read_only=True)
    card_type = serializers.CharField(read_only=True)    
    exp_date = serializers.CharField(read_only=True)
    cvv_no = serializers.CharField(read_only=True)
    balance = serializers.IntegerField(read_only=True)
    payments = serializers.IntegerField(read_only=True)
    verified = serializers.BooleanField(read_only=True)
    
class DashboardStatsSerializer(serializers.Serializer):
    total_payments = serializers.IntegerField(read_only=True)
    invoice_sent = serializers.IntegerField(read_only=True)
    invoice_received = serializers.IntegerField(read_only=True)
    
class DashboardLatestActionsSerializer(serializers.Serializer):
    payment_type = serializers.CharField(read_only=True)
    payment_datetime = serializers.DateTimeField(read_only=True)
    account_holder_name = serializers.CharField(read_only=True)
    bank_name = serializers.CharField(read_only=True)
    bank_branch_name = serializers.CharField(read_only=True)
    ifsc_code = serializers.CharField(read_only=True)
    transaction_amount = serializers.IntegerField(read_only=True)    
    transaction_id = serializers.CharField(read_only=True)
    transaction_status = serializers.CharField(read_only=True)