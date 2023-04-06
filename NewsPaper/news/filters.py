from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            # поиск по названию
            'title': ['icontains'],
            #'author': ['icontains'],
            # количество товаров должно быть больше или равно
            'pub_date': ['gt'],
        }
