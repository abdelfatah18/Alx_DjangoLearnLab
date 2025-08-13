from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
    # Create a new comment for a specific post
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),

    # Update an existing comment
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),

    # Delete an existing comment
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

