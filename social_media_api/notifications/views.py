from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    data = [{"actor": notification.actor.username, "verb": notification.verb, "timestamp": notification.timestamp} for notification in notifications]
    return JsonResponse(data, safe=False)
