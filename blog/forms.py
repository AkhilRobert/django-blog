from django import forms
from django_editorjs_fields import EditorJsWidget
from .models import Blog


class PostCreateUpdateFrom(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "content",
        )
        widgets = {
            "content": EditorJsWidget(
                plugins=[
                    "@editorjs/image",
                    "@editorjs/header",
                    "@editorjs/code",
                    "@editorjs/quote",
                ],
                config={
                    "width": "100%",
                },
            ),
        }
