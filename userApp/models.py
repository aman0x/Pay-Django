from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import IntegrityError

ACCOUNT_TYPE = (
    ("INDIVIDUAL", "Individual"),
    ("BUSINESS", "Business")
)

class CustomUser(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    phone = PhoneNumberField(unique=True,blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
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
    custom_user = models.OneToOneField(
        User, related_name="custom_user", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.email)

    def save(self, *args, **kwargs):
        if not self.pk:
            # If the CustomUser object is being created for the first time
            try:
                if self.email is not None and self.is_social_login is True:
                    user = User.objects.create_user(
                        username=self.email, password='Test@!Test123')
                    self.custom_user = user
                elif self.email is not None and self.is_social_login is False:
                    user = User.objects.create_user(
                        username=self.email, password=self.password)
                    self.custom_user = user
                else:
                    user = User.objects.create_user(
                        username=self.email, password='Test@!Test123')
                    self.custom_user = user
                    
            except IntegrityError:
                # If a user with the same username already exists, retrieve the existing user and update its fields
                user = User.objects.get(username=self.email)
                if self.is_social_login is True:
                    user.set_password('Test@!Test123')
                    user.save()
                    self.custom_user = user
                else:
                    user.set_password(self.password)
                    user.save()
                    self.custom_user = user
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
