from django.contrib import admin
from transactionApp.models import Transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class ReceivableNameFilter(admin.SimpleListFilter):
    title = 'receivable name'
    parameter_name = 'receivable_user'

    def lookups(self, request, model_admin):
        users = set([t.receivable_user for t in model_admin.model.objects.all()])
        return [(user.id, user.username) for user in users]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(receivable_user__id=self.value())
        return queryset

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_amount', 'receivable_user_username', 'transaction_type', 'card', 'bank_account', 'created_at']
    list_filter = ['transaction_type', 'created_at', ReceivableNameFilter]
    search_fields = ['receivable_user__username', 'card__card_holder_name', 'bank_account__account_name']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('receivable_user', 'card', 'bank_account')
        return queryset

    def receivable_user_username(self, obj):
        return obj.receivable_user.username
    receivable_user_username.admin_order_field = 'receivable_user'
    receivable_user_username.short_description = 'Receivable Name'

admin.site.register(Transaction, TransactionAdmin)
