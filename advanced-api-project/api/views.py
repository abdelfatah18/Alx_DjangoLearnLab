from datetime import datetime
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# ✅ List all books (Public)
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
    search_fields = ['title', 'author__name']  # author__name if Author is a ForeignKey

    # ✅ Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']


# ✅ Retrieve one book (Public)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# ✅ Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# ✅ Update a book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.now())


# ✅ Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
