from django.contrib import admin
from .models import BlogModel


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "get_comments_count",
        "get_likes_count",
    )
