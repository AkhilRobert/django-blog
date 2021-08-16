from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import UserModel


@admin.register(UserModel)
class UseerAdmin(ModelAdmin):
    pass
