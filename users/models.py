from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models    

from phonenumber_field.modelfields import PhoneNumberField, PhoneNumber  

from . import managers

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    mobile_phone = PhoneNumberField(unique=True)
    landline_phone = PhoneNumberField(null=True, blank=True)

    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address_number = models.PositiveIntegerField()
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.PositiveIntegerField()

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = "user_profiles"
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
