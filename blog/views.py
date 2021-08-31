from typing import Any, Dict
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from comments.models import Comment
from comments.forms import CreateCommentForm
from .models import Blog
from .forms import PostCreateUpdateFrom


class Home(ListView):
    queryset = (
        Blog.objects.filter(is_private=False)
        .all()
        .order_by("-created_at")
        .prefetch_related("user")
    )
    template_name = "blog/index.html"
    context_object_name = "blog"
    paginate_by = 10


class BlogDetail(DetailView):
    model = Blog
    template_name = "blog/detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        blog = context.get("blog")
        comments = (
            Comment.objects.filter(blog__pk=blog.pk)
            .order_by("-created_at")
            .all()
            .prefetch_related("user")
        )
        context["form"] = CreateCommentForm
        context["comments"] = comments

        return context


class CreatePost(CreateView):
    model = Blog
    template_name = "blog/create.html"
    form_class = PostCreateUpdateFrom

    def form_valid(self, form: PostCreateUpdateFrom) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.success_url = reverse(
            "blog:edit",
            kwargs={
                "pk": self.object.pk,
            },
        )
        return super().form_valid(form)


class EditPost(UpdateView):
    model = Blog
    template_name = "blog/update.html"
    form_class = PostCreateUpdateFrom

    def form_valid(self, form: PostCreateUpdateFrom) -> HttpResponse:
        self.success_url = reverse(
            "blog:edit",
            kwargs={
                "pk": self.object.pk,
            },
        )
        return super().form_valid(form)
