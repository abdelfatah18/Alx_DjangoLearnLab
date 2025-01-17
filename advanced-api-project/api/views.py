from rest_framework import generics, filters  # Import generics for ListView and filters for search & ordering
from django_filters import rest_framework as django_filters  # Import django_filters for filtering support
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by title, author (via author name), and publication_year
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search functionality for title and author name
    search_fields = ['title', 'author__name']

    # Ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']
