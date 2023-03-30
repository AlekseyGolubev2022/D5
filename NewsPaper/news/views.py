from django.views.generic import ListView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-pub_date'
    template_name = 'post_list.html'
    context_object_name = 'posts'