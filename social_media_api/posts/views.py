from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create Like
        Like.objects.create(user=request.user, post=post)

        # Create Notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if not like.exists():
            return Response({"detail": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete Like
        like.delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)

class MarkNotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, notification_id):
        notification = Notification.objects.get(id=notification_id)
        if notification.recipient != request.user:
            return Response({"detail": "You can't mark this notification as read."}, status=status.HTTP_400_BAD_REQUEST)

        notification.is_read = True
        notification.save()

        return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
