from rest_framework import viewsets, permissions, status, views
from .serializers import *
from paymentApp.models import Payment
from rest_framework.response import Response

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
class PaymentDashboardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "all_payments" : 1200,
            "successful" : 12,
            "in_progress" : 122,
            "failed" : 123,
            "refunded" : 123,
            "today_successful" : 4,
            "today_in_progress" : 1,
            "today_failed" : 2,
            "today_refunded" : 0,
        }
        serializer = PaymentDashboardSerializer(data)
        return Response(serializer.data)
    
class PaymentAllPaymentsViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "beneficiary": "Rajesh Kumar",
            "type" : "Vendor_Payment",
            "bank": "HDFC Bank",
            "transaction_id" : "TD136347383DR82",
            "status" : "Succeeded",
            "sum": 24000.24
        }
        serializer = PaymentAllPaymentsSerializer(data)
        return Response(serializer.data)
    
class PaymentDetailsViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "status" : "Succeeded",
            "payment_title" : "Vendor_Payment",
            "transaction_id" : "TD136347383DR82",
            "date" : "2024-06-21T10:21:17.116232Z",
            "phone_number" : "+919573749630",
            "email" : "customer@mail.com",
            "account_number" : "50100350093919",
            "bank" : "HDFC Bank",
            "bank_branch" : "KODAD",
            "ifsc_code" : "HDFC0001642",
            "payment_amount" : 21800,
            "convenience_fee" : 1000,
            "tax" : 1200.24,
            "payment_total_amount" : 24000.24,
        }
        serializer = PaymentDetailsSerializer(data)
        return Response(serializer.data)