from django.contrib import admin
from cardApp.models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_holder_name', 'card_no', 'expiry_date', 'status', 'verified_at', 'created_at']
    list_filter = ['status', 'verified_at', 'created_at']
    search_fields = ['user__username', 'card_holder_name', 'card_no']

admin.site.register(Card, CardAdmin)
