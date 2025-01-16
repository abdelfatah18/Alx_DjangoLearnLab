from rest_framework import generics  # ✅ Import generics
from relationship_app.models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  # ✅ Extends ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
