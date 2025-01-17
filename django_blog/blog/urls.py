from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('search/', views.post_search, name='post-search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='tagged-posts'),
    path('post/<int:pk>/', post_detail, name='post-detail'),  # Post detail view
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # New comment view
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Update comment view
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete comment view
]
