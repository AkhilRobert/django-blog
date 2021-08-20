from django.urls import path
from .views import register, verify_user, LoginUser

app_name = "user"

urlpatterns = [
    path("register/", register, name="register"),
    path("verify/<uuid:token>", verify_user, name="verify"),
    path("login/", LoginUser.as_view(), name="login"),
]
