from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book
from api.serializers import BookSerializer
from django.urls import reverse

class BookAPITestCase(APITestCase):
    """Test suite for CRUD operations on the Book model."""

    def setUp(self):
        """Set up test data before each test."""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2022)
        self.client.login(username="testuser", password="password123")

    def test_list_books(self):
        """Test retrieving all books."""
        url = reverse('book-list')  # Ensure your urls.py has this name for the ListView
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        """Test retrieving a single book by ID."""
        url = reverse('book-detail', kwargs={"pk": self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book(self):
        """Test creating a new book."""
        url = reverse('book-list')
        data = {"title": "New Book", "author": "New Author", "publication_year": 2023}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating an existing book."""
        url = reverse('book-detail', kwargs={"pk": self.book1.id})
        data = {"title": "Updated Title", "author": "Updated Author", "publication_year": 2021}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse('book-detail', kwargs={"pk": self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

## Running Unit Tests for Django REST Framework API

### Prerequisites
Ensure you have:
- Django installed (`pip install django`)
- Django REST Framework installed (`pip install djangorestframework`)

### Running Tests
To run the tests, execute the following command:
```bash
python manage.py test api



