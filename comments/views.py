from django.shortcuts import redirect
from django.urls import reverse
from django.http.request import HttpRequest
from django.views import View
from blog.models import Blog
from .forms import CreateCommentForm


class CreateComment(View):
    def post(self, request: HttpRequest, pk: int):
        form = CreateCommentForm(request.POST)
        blog = Blog.objects.get(pk=pk)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()

        return redirect(reverse("blog:detail", kwargs={"pk": pk}))
