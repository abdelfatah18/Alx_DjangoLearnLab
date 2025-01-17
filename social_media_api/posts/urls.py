from django.urls import path
from .views import like_post, unlike_post

urlpatterns = [
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
