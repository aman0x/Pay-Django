from django.contrib import admin
from transactionApp.models import Transaction, Beneficiary

class BeneficiaryFilter(admin.SimpleListFilter):
    title = 'beneficiary'
    parameter_name = 'beneficiary'

    def lookups(self, request, model_admin):
        beneficiaries = set([t.beneficiary for t in model_admin.model.objects.all()])
        return [(beneficiary.id, beneficiary.name) for beneficiary in beneficiaries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(beneficiary__id=self.value())
        return queryset

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_amount', 'beneficiary_name', 'transaction_type', 'card', 'bank_account', 'created_at']
    list_filter = ['transaction_type', 'created_at', BeneficiaryFilter]
    search_fields = ['beneficiary__name', 'card__card_holder_name', 'bank_account__account_name']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('beneficiary', 'card', 'bank_account')
        return queryset

    def beneficiary_name(self, obj):
        return obj.beneficiary.name
    beneficiary_name.admin_order_field = 'beneficiary'
    beneficiary_name.short_description = 'Beneficiary Name'

admin.site.register(Transaction, TransactionAdmin)
