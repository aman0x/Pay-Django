from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models, IntegrityError
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

ACCOUNT_TYPE = (
    ("INDIVIDUAL", "Individual"),
    ("BUSINESS", "Business")
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = PhoneNumberField(unique=True, blank=True, null=True)
    pan_no = models.CharField(max_length=200, blank=True, null=True)
    adhaar_no = models.CharField(max_length=12, default=None, blank=True, null=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE, default="INDIVIDUAL")
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_pan_no = models.CharField(max_length=200, blank=True, null=True)
    company_adhaar_no = models.CharField(max_length=12, default=None, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    is_social_login = models.BooleanField(default=False)
    social_login_uid = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="custom_auth_user", on_delete=models.CASCADE, null=True, blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class Kyc(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    document_name = models.CharField(max_length=200)
    document_id = models.CharField(max_length=200)
    document_image = models.ImageField(
        upload_to="images/kyc/%y/%m/%d", default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


ACCOUNT_TYPE_CHOICES = (
    ("SAVINGS", "Savings"),
    ("CURRENT", "Current")
)

ACCOUNT_TYPE_2_CHOICES = (
    ("PERSONAL", "Personal"),
    ("BUSINESS", "Business")
)

class BankAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bank_accounts', on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='added_bank_accounts', on_delete=models.SET_NULL, null=True, blank=True)
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    account_type = models.CharField(max_length=20)
    account_type_2 = models.CharField(max_length=20, blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.account_name} - {self.account_number}"
