from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # ✅ URL pattern correctly maps to BookList
]
