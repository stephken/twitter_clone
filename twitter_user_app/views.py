from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitter_user_app import forms, models
from tweet_app import models
from django.contrib.auth import login
from notification_app.models import  Notification

# Create your views here.
def user_profile(request, user_id):
    profile = models.TwitterUser.objects.get(id=user_id)
    tweets = models.Tweet.objects.filter(twitter_user=profile)
    user_following = request.user.following.all()
    following_list = list(user_following)
    return render(request, "user_profile.html",
                  {"profile": profile,
                   "tweets": tweets,
                   "user_following": following_list
                  }
                  )


@login_required
def index_view(request):
    tweets = models.Tweet.objects.filter(twitter_user=request.user)
    following_tweets = models.Tweet.objects.filter(twitter_user__in=request.user.following.all())
    user_following_tweets = tweets | following_tweets
    user_following_tweets = user_following_tweets.order_by('-time_date')
    count = len(
        [notified for notified in Notification.objects.filter(receiver__id=request.user.id) if not notified.viewed_at]
        )
    return render(request, 'index.html', {"Welcome": "Welcome to my Twitter Clone", "tweets": user_following_tweets, "count": count})


def create_user(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = models.TwitterUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password")
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))
    form = forms.SignupForm()
    return render(request, "generic_form.html", {"form": form})

@login_required
def following_view(request, following_id):
    current_user = request.user
    follow = models.TwitterUser.objects.filter(id=following_id).first()
    current_user.following.add(follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def unfollow_view(request, unfollow_id):
    current_user = request.user
    follow = models.TwitterUser.objects.filter(id=unfollow_id).first()
    current_user.following.remove(follow)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))