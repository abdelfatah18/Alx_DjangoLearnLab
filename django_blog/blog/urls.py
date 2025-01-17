from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('post/<int:pk>/', post_detail, name='post-detail'),  # Post detail view
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # New comment view
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Update comment view
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete comment view
]
