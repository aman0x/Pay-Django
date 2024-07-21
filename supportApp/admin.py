# admin.py

from django.contrib import admin
from .models import ContactSubmission, FAQ

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('topic', 'heading')
    search_fields = ('topic', 'heading', 'subtext')
    list_filter = ('topic',)
