from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Verification


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Verification)
class VerificationAdmin(ModelAdmin):
    list_display = (
        "token",
        "token_valid",
    )
