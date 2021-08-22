from django.views.generic import ListView
from .models import Blog


class Home(ListView):
    queryset = Blog.objects.filter().all()
    template_name = "blog/index.html"
    context_object_name = "blog"
    paginate_by = 10
