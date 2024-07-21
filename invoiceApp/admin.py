from django.contrib import admin
from .models import Service, Invoice

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'receiver', 'amount', 'tax', 'status', 'invoice_number', 'created_at')
    search_fields = ('user__username', 'receiver__username', 'invoice_number')
    list_filter = ('status', 'created_at')
    filter_horizontal = ('services',)
    readonly_fields = ('invoice_number',)
