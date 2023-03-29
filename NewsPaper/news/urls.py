from django.urls import path
from .views import PostsList

app_name = 'news'

urlpatterns = [
   path('', PostsList.as_view()),
]