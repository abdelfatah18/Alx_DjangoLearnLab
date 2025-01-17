from django.urls import path
from .views import post_detail, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('post/<int:pk>/', post_detail, name='post-detail'),  # Post detail view
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create new comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Edit comment view
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete comment view
]
