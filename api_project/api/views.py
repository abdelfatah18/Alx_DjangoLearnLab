from rest_framework import generics, viewsets  # ✅ Import viewsets
from relationship_app.models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated  # ✅ Import permission class

# ✅ Existing ListAPIView (Keep it if needed)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ New ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):  # ✅ Extends ModelViewSet
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Add permission class for authentication
