# serializers.py
from rest_framework import serializers
from supportApp.models import ContactSubmission, FAQ

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']



class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'topic', 'heading', 'subtext']
