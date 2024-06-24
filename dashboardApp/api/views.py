from rest_framework import viewsets, views
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
from django.db import models

class DashboardQuickSendViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "name": "Jane Smith",
            "username": "@jane_smith"
        }
        serializer = DashboardQuickSendSerializer(data)
        return Response(serializer.data)
    
class DashboardTotalMonthSpendingsViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "card_number": "1234567824681257",
            "card_type": "VISA",
            "incomes": "10000",
            "expenses": "9000"
        }
        serializer = DashboardTotalMonthSpendingsSerializer(data)
        return Response(serializer.data)
    
class DashboardMyTemplateViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "bank_name": "HDFC Bank",
            "bank_branch_name": "KODAK",
            "account_holder_name": "ANANTHARAPU ARUNA THEJASWINI",
            "ifsc_code": "HDFC000162"
        }
        serializer = DashboardMyTemplateSerializer(data)
        return Response(serializer.data)
    
class DashboardMyCardViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "card_holder_name" : "ANANTHARAPU ARUNA THEJASWINI",
            "card_number" : "1234567824681257",
            "card_type" : "VISA",
            "exp_date" : "02/28",
            "cvv_no" : "123",
            "balance" : 12000,
            "payments" : 12,
            "verified" : True
        }
        serializer = DashboardMyCardSerializer(data)
        return Response(serializer.data)
    
class DashboardStatsViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "total_payments": 240000.70,
            "invoice_sended": 12,
            "invoice_received": 2
        }
        serializer = DashboardStatsSerializer(data)
        return Response(serializer.data)

class DashboardLatestActionsViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "payment_type" : "Vendor_Payment",
            "payment_datetime" : "2024-06-21T10:21:17.116232Z",
            "account_holder_name" : "ANANTHARAPU ARUNA THEJASWINI",
            "bank_name": "HDFC Bank",
            "bank_branch_name": "KODAK",
            "ifsc_code": "HDFC000162",
            "transaction_amount" : 100000,
            "transaction_id" : "TD136347383DR82",
            "transaction_status" : "In Progress",
        }
        serializer = DashboardLatestActionsSerializer(data)
        return Response(serializer.data)