from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Like
from django.contrib.auth.decorators import login_required

# Like a post
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    # You can add a notification for liking a post here if needed
    if created:
        # Logic to create a notification for the user who liked the post
        pass

    return JsonResponse({'message': 'Post liked successfully!'})

# Unlike a post
@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()

        # Logic to create a notification for unliking the post
        pass
    except Like.DoesNotExist:
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)

    return JsonResponse({'message': 'Post unliked successfully!'})
