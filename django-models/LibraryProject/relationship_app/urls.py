from django.urls import path
from .views import list_books 
from .views import LibraryDetailView
from . import views

from django.contrib.auth.views import LoginView, LogoutView

from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', views.home, name='home'),
]




