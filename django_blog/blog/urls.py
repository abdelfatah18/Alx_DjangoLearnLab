# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegistrationView, profile_view

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    # Add other URL patterns as needed
]
