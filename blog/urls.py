from django.urls import path
from .views import Home, BlogDetail

app_name = "blog"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("blog/<int:pk>", BlogDetail.as_view(), name="detail"),
]
