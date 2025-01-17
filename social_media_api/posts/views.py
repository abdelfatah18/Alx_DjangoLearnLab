from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer

class UserFeedView(generics.ListAPIView):
    """Returns posts from followed users, ordered by creation date."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Returns posts from users that the current user follows."""
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
