from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="liked your post",
            target=post
        )
        return Response({'message': 'Post liked successfully.'}, status=200)
    else:
        return Response({'message': 'You have already liked this post.'}, status=400)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(post=post, user=request.user)
    if like.exists():
        like.delete()
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="unliked your post",
            target=post
        )
        return Response({'message': 'Post unliked successfully.'}, status=200)
    else:
        return Response({'message': 'You have not liked this post.'}, status=400)
