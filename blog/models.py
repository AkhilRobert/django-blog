from django.db import models
from django_quill.fields import QuillField
from users.models import UserModel


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    content = QuillField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return self.title
