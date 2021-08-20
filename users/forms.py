from uuid import uuid4 as uuid
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Verification


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(),
        label="password",
    )
    password2 = None

    def save(self, commit: bool = True):
        verification = Verification(token=uuid())
        verification.save()

        user: User = super().save(commit=commit)
        user.verification_token = verification
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )
