from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ✅ List all books (Public)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# ✅ Retrieve one book (Public)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# ✅ Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # You must have a 'created_by' field in your Book model
        serializer.save(created_by=self.request.user)

# ✅ Update a book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # You must have an 'updated_at' field in your Book model
        serializer.save(updated_at=datetime.now())

# ✅ Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
