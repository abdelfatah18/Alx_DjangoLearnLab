# LibraryProject

## مقدمة
هذا المشروع يهدف إلى تعليم ميزات Django المتقدمة والأمان.

## إعداد الأذونات والمجموعات

### الأذونات المخصصة
- `can_view`: يمكنه عرض المستخدمين
- `can_create`: يمكنه إنشاء المستخدمين
- `can_edit`: يمكنه تعديل المستخدمين
- `can_delete`: يمكنه حذف المستخدمين

### المجموعات والأذونات
- **Editors**: `can_create`, `can_edit`
- **Viewers**: `can_view`
- **Admins**: `can_create`, `can_edit`, `can_delete`, `can_view`

### تطبيق الأذونات في العروض
استخدم `@permission_required` للتحقق من الأذونات في العروض. مثال:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request, user_id):
    # منطق التعديل هنا
    return render(request, 'edit_user.html')
