# views.py
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from supportApp.models import ContactSubmission, FAQ
from .serializers import ContactSubmissionSerializer, FAQSerializer
from django.conf import settings

class ContactSubmissionView(APIView):
    def post(self, request, format=None):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupportInfoView(APIView):
    def get(self, request, format=None):
        support_info = settings.SUPPORT_INFO
        return Response(support_info, status=status.HTTP_200_OK)

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic', 'heading', 'subtext']
