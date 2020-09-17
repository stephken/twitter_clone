from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from twitter_user_app import forms, models
from tweet_app import models
from django.contrib.auth import login
from notification_app.models import  Notification
from django.views.generic import TemplateView

#  Create your views here.
class user_profile(TemplateView):

    def get(self, request, user_id):
        profile = models.TwitterUser.objects.get(id=user_id)
        tweets = models.Tweet.objects.filter(twitter_user=profile)
        user_following = profile.following.all()
        following_list = list(user_following)
        return render(request, 'profile.html', {'profile': profile, 'tweets': tweets, 'user_following': following_list})


class index_view(LoginRequiredMixin, TemplateView):

    def get(self, request):
        tweets = models.Tweet.objects.filter(twitter_user=request.user)
        following_tweets = models.Tweet.objects.filter(twitter_user__in=request.user.following.all())
        user_following_tweets = tweets | following_tweets
        user_following_tweets = user_following_tweets.order_by('-time_date')
        count = len(
            [notified for notified in Notification.objects.filter(receiver__id=request.user.id) if not notified.viewed_at]
            )
        return render(request, 'index.html', {'Welcome': 'Welcome to my Twitter Clone', 'tweets': user_following_tweets, 'count': count})


class create_user(TemplateView):

    def get(self, request):
        form = forms.SignupForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = models.TwitterUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request, 'generic_form.html', {'form': form})

class following_view(LoginRequiredMixin, TemplateView):

    def get(self, request, following_id):
        current_user = request.user
        follow = models.TwitterUser.objects.filter(id=following_id).first()
        current_user.following.add(follow)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class unfollow_view(LoginRequiredMixin, TemplateView):

    def get(self, request, unfollow_id):
        current_user = request.user
        follow = models.TwitterUser.objects.filter(id=unfollow_id).first()
        current_user.following.remove(follow)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))