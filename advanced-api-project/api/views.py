from rest_framework import generics, filters
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
