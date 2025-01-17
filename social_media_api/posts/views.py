from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import permissions
from .models import Post, Like, Notification
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes

# Like a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user has already liked the post
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    # Create a notification for the post like
    if created:
        Notification.objects.create(user=request.user, post=post, action='liked')

    return JsonResponse({'message': 'Post liked successfully!'})

# Unlike a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    try:
        # Attempt to retrieve and delete the like
        like = Like.objects.get(user=request.user, post=post)
        like.delete()

        # Create a notification for unliking the post
        Notification.objects.create(user=request.user, post=post, action='unliked')

    except Like.DoesNotExist:
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)

    return JsonResponse({'message': 'Post unliked successfully!'})
