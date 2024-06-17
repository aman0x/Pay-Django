from rest_framework import viewsets, permissions, status
from .serializers import SupportSerializer
from supportApp.models import Support

class SupportViewSet(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]