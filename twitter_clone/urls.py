"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitter_user_app import views as twitter_user_views
from authentication_app import views as authentication_views
from tweet_app import views as tweet_views
from notification_app import views as notification_views

urlpatterns = [
    path('', twitter_user_views.index_view, name="home"),
    path('profile/<int:user_id>/', twitter_user_views.user_profile, name="profile"),
    path('tweet/<int:tweet_id>/', tweet_views.tweet_view, name="tweet"),
    path('addtweet/', tweet_views.create_tweet, name="addtweet"),
    path('notification/<int:user_id>/', notification_views.notification_view, name="notification" ),
    path('follow/<int:following_id>/', twitter_user_views.following_view, name="follow" ),
    path('unfollow/<int:unfollow_id>/', twitter_user_views.unfollow_view, name="unfollow" ),
    path('login/', authentication_views.login_view, name="login"),
    path('logout/', authentication_views.logout_view, name="logout"),
    path('signup/', twitter_user_views.create_user, name="signup"),
    path('admin/', admin.site.urls),
]
