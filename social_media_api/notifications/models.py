from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    ACTION_CHOICES = [
        ('liked', 'Liked'),
        ('unliked', 'Unliked'),
        # Add other actions as necessary
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action} post {self.post.id}"
