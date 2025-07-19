from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # الأعمدة الظاهرة في قائمة الكتب
    list_filter = ('publication_year',)  # فلتر جانبي حسب سنة النشر
    search_fields = ('title', 'author')  # تمكين البحث بالعنوان والمؤلف
