# serializers.py
from rest_framework import serializers
from supportApp.models import ContactSubmission, FAQ

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

class FAQSerializer(serializers.ModelSerializer):
    topic_display = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'topic', 'heading', 'subtext', 'topic_display']

    def get_topic_display(self, obj):
        return obj.get_topic_display()
