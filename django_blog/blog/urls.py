# blog/urls.py
from django.urls import path
from .views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),  # Define the view for profile management
]
