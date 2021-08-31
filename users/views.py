import os
from typing import Any, Dict
from uuid import UUID
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.utils.html import strip_tags
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm
from .models import User, Verification


def register(request: HttpRequest) -> HttpRequest:
    if request.user.is_authenticated:
        return redirect(reverse("blog:home"))

    form = RegisterForm()
    next = request.GET.get("next", None)

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            if next is None:
                return redirect(reverse("blog:home"))

            return redirect(next)

    return render(
        request,
        "users/register.html",
        {
            "form": form,
        },
    )


def verify_user(request: HttpRequest, token: UUID) -> HttpRequest:
    verfiy_token: Verification = Verification.objects.filter(token=token).first()
    if verfiy_token is None:
        return render(request, "users/verify/error.html")

    if not verfiy_token.token_valid:
        return render(request, "users/verify/error.html")

    user: User = User.objects.get(verification_token=verfiy_token)
    user.is_verified = True
    user.save()
    verfiy_token.delete()
    return render(request, "users/verify/success.html")


# TODO: Implement this
class SendVerification(View):
    def get(self, requset: HttpRequest):
        if requset.user.is_anonymous:
            return redirect(reverse("users:login"))

        user: User = requset.user
        if user.is_verified:
            return redirect(reverse("blog:home"))

    pass

    # TODO: Check if properly implemented
    def post(self, request: HttpRequest):

        html_mail = render_to_string(
            "users/mail.html",
            {
                "token": request.user.verification_token,
            },
        )
        plain_mail = strip_tags(html_mail)

        send_mail(
            "Verify your account",
            plain_mail,
            os.environ.get("SENDER_MAIL"),
            [request.user.email],
            html_message=html_mail,
            fail_silently=True,
        )


class LoginUser(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("blog:home")
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["next"] = self.request.GET.get("next")
        return context


class LogoutUser(LogoutView):
    pass
