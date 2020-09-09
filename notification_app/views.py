from django.shortcuts import render
from django.utils import timezone
from notification_app.models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def notification_view(request, user_id):
    notifications = Notification.objects.filter(receiver__id=user_id).filter(viewed_at=None)
    # received_notification = []
    for notified in notifications:
    #     if notified.viewed_at:
    #         received_notification.append(notified.tweet)
         notified.viewed_at = timezone.now()
         notified.save()
    return render(request, "notification_view.html",{"received_notification": notifications})

