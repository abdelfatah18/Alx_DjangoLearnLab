import sqlite3

# تأكد من تحديث مسار قاعدة البيانات الخاصة بك
db_path = 'db.sqlite3'  # تأكد من أن هذا المسار يتطابق مع مسار قاعدة البيانات الخاصة بك

# الاتصال بقاعدة البيانات
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# الحصول على جميع أسماء الجداول
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# حذف جميع الجداول باستثناء جدول sqlite_sequence
for table in tables:
    if table[0] != 'sqlite_sequence':
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")

# إغلاق الاتصال
conn.commit()
conn.close()

print("تم حذف جميع الجداول المحددة بنجاح.")