from django.db import models
from django_quill.fields import QuillField
from users.models import UserModel


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    content = QuillField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserModel, related_name="likes", blank=True)

    def __str__(self):
        return self.title

    def get_likes_count(self):
        return self.likes.all().count()

    def get_comments_count(self):
        return self.comments.all().count()

    class Meta:
        verbose_name_plural = "blogs"
