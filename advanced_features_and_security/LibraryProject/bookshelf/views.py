from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    # Your logic for creating a book
    pass

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Your logic for editing a book
    pass

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Your logic for deleting a book
    pass
