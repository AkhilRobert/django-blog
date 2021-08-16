from django.contrib import admin
from .models import BlogModel


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    pass
