import requests
from django.conf import settings
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CardSerializer, BinCheckSerializer
from cardApp.models import Card

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['card_holder_name', 'card_no']
    ordering_fields = ['created_at', 'modified_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Card.objects.filter(user=self.request.user, deleted=False)
        return Card.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def delete_card(self, request, pk=None):
        try:
            card = self.get_queryset().get(pk=pk)
            card.deleted = True
            card.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Card.DoesNotExist:
            return Response({'error': 'Card not found'}, status=status.HTTP_404_NOT_FOUND)

class BinCheckView(APIView):
    def get(self, request, bin_code, format=None):
        serializer = BinCheckSerializer(data={'bin_code': bin_code})
        if serializer.is_valid():
            bin_code = serializer.validated_data['bin_code']
            url = f"https://api.apilayer.com/bincheck/{bin_code}"
            headers = {
                "apikey": settings.APILAYER_API_KEY
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            return Response(response.json(), status=response.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
