from django.urls import path
from . import views

urlpatterns = [
    # Existing URLs
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    # Add other URLs for creating, updating, and deleting posts

    # URL for viewing posts by tag
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),

    # URL for handling search functionality
    path('search/', views.search_posts, name='search-posts'),
]
