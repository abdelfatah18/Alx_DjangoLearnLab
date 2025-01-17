from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from notifications.models import Notification

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if Like.objects.filter(post=post, user=request.user).exists():
        return JsonResponse({'message': 'You have already liked this post.'}, status=400)
    Like.objects.create(post=post, user=request.user)
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
    like.delete()
    Notification.objects.create(
        recipient=post.user,
        actor=request.user,
        verb="unliked your post",
        target=post
    )
    return JsonResponse({'message': 'Post unliked successfully.'}, status=200)
