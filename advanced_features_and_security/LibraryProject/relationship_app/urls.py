from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),  # استخدم العرض المخصص هنا
    path('logout/',LogoutView.as_view(template_name='login.html'), name='logout'),  # استخدم العرض المخصص هنا
    path('register/',views.register_view, name='register'),
    path('home/',views.home, name='home'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book_view, name='delete_book'),
]
