from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # رابط التسجيل
    path('register/', views.register, name='register'),
    
    # رابط تسجيل الدخول
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # رابط تسجيل الخروج
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    
    # يمكنك إضافة المزيد من الروابط هنا حسب احتياجك
    path('', views.home, name='home'),
]




