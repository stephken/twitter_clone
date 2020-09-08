from django.db import models
from tweet_app.models import Tweet
from twitter_user_app.models import TwitterUser

# Create your models here.
class Notification(models.Model):
    receiver = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name="receive")
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet_received")
    viewed_at = models.DateTimeField(default=None, blank=True, null=True)