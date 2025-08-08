from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ✅ List all books (Public)
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    GET /api/books/?search=python&ordering=title&publication_year=2023
    Supports: Filtering, Searching, Ordering
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    # ✅ Add filtering/searching/ordering support
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Filter by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # ✅ Search in these fields
    search_fields = ['title', 'author__name']  # إذا كانت author علاقة ForeignKey

    # ✅ Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

    

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
