from django.shortcuts import render, get_object_or_404
from bookshelf.models import Book
from .forms import ExampleForm  # Add this import statement

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    # Your edit logic here
    return render(request, 'edit_user.html', {'user': user})
