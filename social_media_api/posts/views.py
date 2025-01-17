# posts/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Check if the user has already liked the post
    if Like.objects.filter(post=post, user=request.user).exists():
        return JsonResponse({'message': 'You have already liked this post.'}, status=400)
    
    # Create the like
    Like.objects.create(post=post, user=request.user)

    # Create notification
    Notification.objects.create(
        recipient=post.user,
        actor=request.user,
        verb="liked your post",
        target=post
    )

    return JsonResponse({'message': 'Post liked successfully.'}, status=200)

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(post=post, user=request.user)
    
    if not like.exists():
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)

    # Delete the like
    like.delete()

    # Create notification for unliking (optional, depending on your use case)
    Notification.objects.create(
        recipient=post.user,
        actor=request.user,
        verb="unliked your post",
        target=post
    )

    return JsonResponse({'message': 'Post unliked successfully.'}, status=200)
