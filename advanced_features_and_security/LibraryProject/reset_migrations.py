import sqlite3

# تأكد من تحديث مسار قاعدة البيانات الخاصة بك
db_path = 'db.sqlite3'  # تأكد من أن هذا المسار يتطابق مع مسار قاعدة البيانات الخاصة بك

# الاتصال بقاعدة البيانات
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# حذف جدول django_migrations
cursor.execute("DROP TABLE IF EXISTS django_migrations")

# إغلاق الاتصال
conn.commit()
conn.close()

print("جدول django_migrations تم حذفه بنجاح.")