from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'login.html'  # مسار قالب تسجيل الدخول

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'  # مسار قالب تسجيل الخروج

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def list_books(request):
    books = Book.objects.all()
    if not books:
        messages.info(request, "لا توجد كتب حالياً.")
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # قم بتعديل المسار إذا لزم الأمر
    context_object_name = 'library'



def home(request):
    return render(request, 'home.html')
