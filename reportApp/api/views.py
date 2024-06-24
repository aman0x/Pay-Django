from rest_framework import viewsets, views
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
from django.db import models

class ReportMonthlyReportViewSet(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            "date" : "2024-06-21T10:21:17.116232Z",
            "sent_from": "Rajesh Kumar",
            "type" : "Vendor_Payment",
            "bank": "HDFC Bank",
            "account_type": "Credit",
            "transaction_id" : "TD136347383DR82",
            "status" : "Succeeded",
            "sum": 5000
        }
        serializer = ReportMonthlyReportSerializer(data)
        return Response(serializer.data)