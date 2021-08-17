from django.contrib import admin
from .models import CommentsModel


@admin.register(CommentsModel)
class CommentdAdmin(admin.ModelAdmin):
    pass
