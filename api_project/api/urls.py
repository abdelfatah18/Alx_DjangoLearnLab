from django.urls import path, include  # ✅ Import include
from rest_framework.routers import DefaultRouter  # ✅ Import DefaultRouter
from .views import BookList, BookViewSet  # ✅ Import both views

# ✅ Create a router and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ✅ List view (if needed)
    path('books/', BookList.as_view(), name='book-list'),
    
    # ✅ Include the router-generated URLs
    path('', include(router.urls)),  # This automatically maps CRUD routes
]
