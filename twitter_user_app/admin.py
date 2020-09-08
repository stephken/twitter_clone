from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitter_user_app.models import TwitterUser
# Register your models here.
admin.site.register(TwitterUser, UserAdmin)
