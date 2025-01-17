from django.urls import path
from . import views

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),     
    path('posts/<int:pk>/like/', views.like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', views.unlike_post, name='unlike_post'),
    
]


