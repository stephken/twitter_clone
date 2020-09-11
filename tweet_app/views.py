import re 
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet_app import models, forms
from twitter_user_app.models import TwitterUser
from notification_app.models import Notification
from django.views.generic import TemplateView

# Create your views here.
class tweet_view(TemplateView):

    def get(self, request, tweet_id):
        tweet = models.Tweet.objects.filter(id=tweet_id).first()
        return render(request, 'tweet.html', {'Tweet':tweet})


class create_tweet(LoginRequiredMixin, TemplateView):

    def get(self, request):
        form = forms.TweetForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = forms.TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            at_user = re.findall(r'@([\w]+)', data.get('tweet'))
            new_tweet = models.Tweet.objects.create(
                tweet = data.get('tweet'),
                twitter_user= request.user
            )
            if at_user:
                for at in at_user:
                    new_notification = Notification.objects.create(
                        tweet = new_tweet,
                        receiver = TwitterUser.objects.get(username=at)
                    )
            return HttpResponseRedirect(reverse('home'))