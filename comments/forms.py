from .models import Comment
from django import forms


class CreateCommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Add a comment",
            }
        ),
        label="",
    )

    class Meta:
        model = Comment
        fields = ("body",)
