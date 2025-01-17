from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer

class UserFeedView(generics.ListAPIView):
    """Displays posts from users that the current user follows."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve posts from followed users, ordered by newest first."""
        return Post.objects.filter(author__in=self.request.user.following.all()).order_by('-created_at')

class FollowUserView(generics.GenericAPIView):
    """Allows an authenticated user to follow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    """Allows an authenticated user to unfollow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
