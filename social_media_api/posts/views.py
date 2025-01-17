from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # التحقق من تسجيل دخول المستخدم
def like_post(request, pk):
    # استرجاع الـ post باستخدام generics.get_object_or_404
    post = get_object_or_404(Post, pk=pk)
    
    # الحصول أو إنشاء Like جديد إذا لم يكن موجودًا بالفعل
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
    
    # إنشاء إشعار للمستخدم صاحب المنشور
    Notification.objects.create(
        recipient=post.author,  # الشخص الذي نشر المنشور
        actor=request.user,     # الشخص الذي قام بالإعجاب
        verb="liked your post", # وصف الحدث
        target=post            # الهدف هو المنشور
    )
    
    return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # التحقق من تسجيل دخول المستخدم
def unlike_post(request, pk):
    # استرجاع الـ post باستخدام generics.get_object_or_404
    post = get_object_or_404(Post, pk=pk)

    # التحقق إذا كان المستخدم قد قام بإعجاب المنشور
    like = Like.objects.filter(user=request.user, post=post)
    if not like.exists():
        return Response({"detail": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
    
    # إزالة الإعجاب
    like.delete()
    
    return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
