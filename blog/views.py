from typing import Any, Dict
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from comments.models import Comment
from comments.forms import CreateCommentForm


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
