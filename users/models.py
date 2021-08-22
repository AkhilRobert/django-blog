import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.db.models.fields.related import OneToOneField
from .manager import UserManager


class User(AbstractBaseUser):

    login_types = (
        ("EMAIL", "EMAIL"),
        ("GITHUB", "GITHUB"),
    )

    email = models.EmailField(unique=True, max_length=120)
    username = models.CharField(max_length=120)
    is_verified = models.BooleanField(default=False)
    auth_type = models.CharField(default="EMAIL", choices=login_types, max_length=120)
    is_staff = models.BooleanField(default=False)
    profile_photo = models.ImageField(
        blank=True, null=True, upload_to="profile_photos/"
    )
    verification_token = OneToOneField(
        "Verification",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "auth_type",
        "username",
    ]

    def __str__(self):
        return self.email

    # Premission for the admin page
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # Premission for the admin page
    def has_module_perms(self, app_label):
        return self.is_staff

    class Meta:
        verbose_name_plural = "users"


class Verification(models.Model):
    token = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def token_valid(self) -> bool:
        expiry_time = self.created_at + datetime.timedelta(minutes=10)
        # timezone.localtime() because we want local time ie, Asia/Kolkata
        # timezone.now() returns UTC time
        return expiry_time >= timezone.localtime()

    def __str__(self) -> str:
        return str(self.token)
