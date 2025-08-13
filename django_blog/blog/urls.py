from django.urls import path
from . import views

urlpatterns = [
    # Create a new comment for a specific post
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),

    # Update an existing comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),

    # Delete an existing comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
