from django.contrib import admin
from .models import Service, Invoice

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'beneficiary_name', 'amount', 'tax', 'status', 'invoice_number', 'created_at', 'invoice_type')
    search_fields = ('user__username', 'beneficiary__name', 'invoice_number')
    list_filter = ('status', 'created_at')
    filter_horizontal = ('services',)
    readonly_fields = ('invoice_number',)

    def beneficiary_name(self, obj):
        return obj.beneficiary.name
    beneficiary_name.admin_order_field = 'beneficiary'
    beneficiary_name.short_description = 'Beneficiary Name'
