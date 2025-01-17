from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
def like_post(request, pk):
    # تأكد من أن المستخدم مسجل دخول
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # استرجاع الـ post
    post = get_object_or_404(Post, pk=pk)
    
    # تحقق إذا كان المستخدم قد قام بإعجاب نفس المنشور بالفعل
    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

    # إنشاء الإعجاب
    Like.objects.create(user=request.user, post=post)
    
    # إنشاء إشعار للمستخدم صاحب المنشور
    Notification.objects.create(
        recipient=post.author,  # الشخص الذي نشر المنشور
        actor=request.user,     # الشخص الذي قام بالإعجاب
        verb="liked your post", # وصف الحدث
        target=post            # الهدف هو المنشور
    )
    
    return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unlike_post(request, pk):
    # تأكد من أن المستخدم مسجل دخول
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
    
    # استرجاع الـ post
    post = get_object_or_404(Post, pk=pk)

    # تحقق إذا كان المستخدم قد قام بإعجاب المنشور بالفعل
    like = Like.objects.filter(user=request.user, post=post)
    if not like.exists():
        return Response({"detail": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
    
    # إزالة الإعجاب
    like.delete()
    
    return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
