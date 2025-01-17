# posts/views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth.models import User

@api_view(['POST'])
def like_post(request, pk):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    post = get_object_or_404(Post, pk=pk)
    if Like.objects.filter(post=post, user=request.user).exists():
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    like = Like.objects.create(post=post, user=request.user)

    # Create notification
    Notification.objects.create(
        recipient=post.user,
        actor=request.user,
        verb="liked your post",
        target=post
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unlike_post(request, pk):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(post=post, user=request.user).first()
    if not like:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()

    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
