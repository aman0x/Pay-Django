from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Kyc, BankAccount, Beneficiary, IndividualUser, BusinessUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class IndividualUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'pan_no', 'adhaar_no')
    search_fields = ('user__email', 'pan_no', 'adhaar_no')
    ordering = ('user__email',)

admin.site.register(IndividualUser, IndividualUserAdmin)

class BusinessUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'company_pan_no', 'company_gst_no')
    search_fields = ('user__email', 'company_name', 'company_pan_no', 'company_gst_no')
    ordering = ('user__email',)

admin.site.register(BusinessUser, BusinessUserAdmin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'account_type']
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'account_type')
    ordering = ('email',)
    filter_horizontal = ()
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'middle_name', 'last_name', 'nick_name', 'phone', 'account_type'
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'middle_name', 'last_name', 'nick_name', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'account_type')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class KycAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'region', 'document_name', 'document_id', 'created_at', 'modified_at')
    search_fields = ('user__email', 'name', 'document_name')
    list_filter = ('created_at', 'modified_at')
    ordering = ('-created_at',)

admin.site.register(Kyc, KycAdmin)

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_name', 'account_number', 'ifsc_code', 'account_type', 'bank_name', 'deleted')
    search_fields = ('user__email', 'account_name', 'account_number')
    list_filter = ('account_type', 'account_type_2')
    ordering = ('-account_name',)

admin.site.register(BankAccount, BankAccountAdmin)

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number', 'verified', 'verified_at', 'created_at', 'modified_at')
    search_fields = ('user__email', 'name', 'phone_number')
    list_filter = ('verified', 'verified_at')
    ordering = ('-verified_at',)

admin.site.register(Beneficiary, BeneficiaryAdmin)