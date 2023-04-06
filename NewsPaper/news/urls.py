from django.urls import path

from .views import NewsList, PostDetail

app_name = 'news'

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', NewsList.as_view(), name='news_search'),
]
