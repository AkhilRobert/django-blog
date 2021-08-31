from django.urls import path
from .views import CreateComment

app_name = "comment"

urlpatterns = [
    path("create/<int:pk>", CreateComment.as_view(), name="create_comment"),
]
