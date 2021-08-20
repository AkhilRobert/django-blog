from uuid import UUID
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.utils.html import strip_tags
from .forms import RegisterForm
from .models import User, Verification


def register(request: HttpRequest) -> HttpRequest:
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            html_mail = render_to_string(
                "users/mail.html",
                {
                    "token": user.verification_token,
                },
            )
            plain_mail = strip_tags(html_mail)

            send_mail(
                "Verify your account",
                plain_mail,
                "akhilrobert@outlook.com",
                [user.email],
                html_message=html_mail,
                fail_silently=True,
            )
            return redirect(reverse("blog:home"))

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
