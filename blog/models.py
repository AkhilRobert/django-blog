from django.db import models
from django_editorjs_fields import EditorJsJSONField
from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = EditorJsJSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    def __str__(self):
        return self.title

    @property
    def likes_count(self) -> int:
        return self.likes.all().count()

    @property
    def comments_count(self) -> int:
        return self.comments.all().count()

    class Meta:
        verbose_name_plural = "blogs"
