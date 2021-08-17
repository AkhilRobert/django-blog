from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .manager import UserManager


class UserModel(AbstractBaseUser):

    login_types = (
        ("EMAIL", "EMAIL"),
        ("GITHUB", "GITHUB"),
    )

    email = models.EmailField(unique=True, max_length=120)
    username = models.CharField(max_length=120)
    is_verified = models.BooleanField(default=False)
    auth_type = models.CharField(default="EMAIL", choices=login_types, max_length=120)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["auth_type"]

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
