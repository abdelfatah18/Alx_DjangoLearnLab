from rest_framework import generics, permissions
from posts.models import Post
from posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404

class PostListCreateView(generics.ListCreateAPIView):
    """Allows users to create and list posts."""
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Associates the logged-in user as the author of the post."""
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Allows users to retrieve, update, or delete a post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Ensure users can only edit or delete their own posts."""
        return Post.objects.filter(author=self.request.user)

class UserFeedView(generics.ListAPIView):
    """Displays posts from users that the current user follows."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve posts from followed users, ordered by newest first."""
        return Post.objects.filter(author__in=self.request.user.following.all()).order_by('-created_at')
