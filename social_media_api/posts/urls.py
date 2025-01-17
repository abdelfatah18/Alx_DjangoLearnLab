from django.urls import path
from posts.views import PostListCreateView, PostDetailView, UserFeedView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
