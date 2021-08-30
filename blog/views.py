from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Blog


class Home(ListView):
    queryset = (
        Blog.objects.filter().all().order_by("-created_at").prefetch_related("user")
    )
    template_name = "blog/index.html"
    context_object_name = "blog"
    paginate_by = 10


class BlogDetail(DetailView):
    model = Blog
    template_name = "blog/detail.html"
