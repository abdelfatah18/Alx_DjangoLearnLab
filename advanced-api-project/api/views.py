from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# عرض قائمة الكتب (ListView)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# عرض تفاصيل كتاب واحد (DetailView)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# إنشاء كتاب جديد (CreateView)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # السماح فقط للمستخدمين المسجلين

# تحديث كتاب موجود (UpdateView)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # السماح فقط للمستخدمين المسجلين

# حذف كتاب (DeleteView)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # السماح فقط للمستخدمين المسجلين
