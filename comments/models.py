from django.db import models
from django.db.models.expressions import Case
from users.models import UserModel
from blog.models import BlogModel


class CommentsModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    blog = models.ForeignKey(
        BlogModel, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name_plural = "comments"
