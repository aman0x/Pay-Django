from rest_framework import viewsets, permissions, status
from .serializers import PaymentSerializer
from paymentApp.models import Payment

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]