# from django.http import HttpRequest
# from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


class Home(ListView):
    queryset = Blog.objects.filter(is_private=False).all()
    template_name = "blog/index.html"
    context_object_name = "blog"
