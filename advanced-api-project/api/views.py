from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# عرض قائمة الكتب (عام للجميع)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# عرض تفاصيل كتاب واحد (عام للجميع)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# إنشاء كتاب (للمستخدمين المسجلين فقط)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# تحديث كتاب (للمستخدمين المسجلين فقط)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# حذف كتاب (للمستخدمين المسجلين فقط)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
