from django.urls import path
from .views import Home, BlogDetail, CreatePost, EditPost

app_name = "blog"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("blog/<int:pk>", BlogDetail.as_view(), name="detail"),
    path("blog/create", CreatePost.as_view(), name="create"),
    path("blog/edit/<int:pk>", EditPost.as_view(), name="edit"),
]
