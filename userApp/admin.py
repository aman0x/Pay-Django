from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Kyc, BankAccount, Beneficiary
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'nick_name', 'phone', 'pan_no', 'adhaar_no', 'account_type', 'company_name', 'company_pan_no', 'company_adhaar_no', 'otp', 'is_social_login', 'social_login_uid')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class KycAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'region', 'document_name', 'document_id', 'created_at', 'modified_at')
    search_fields = ('user__email', 'name', 'document_name')
    list_filter = ('created_at', 'modified_at')
    ordering = ('-created_at',)

admin.site.register(Kyc, KycAdmin)

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_name', 'account_number', 'ifsc_code', 'account_type', 'bank_name')
    search_fields = ('user__email', 'account_name', 'account_number')
    list_filter = ('account_type', 'account_type_2')
    ordering = ('-account_name',)

admin.site.register(BankAccount, BankAccountAdmin)

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number', 'verified', 'verified_at')
    search_fields = ('user__email', 'name', 'phone_number')
    list_filter = ('verified', 'verified_at')
    ordering = ('-verified_at',)

admin.site.register(Beneficiary, BeneficiaryAdmin)
