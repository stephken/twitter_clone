from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TwitterUser(AbstractUser):
     following = models.ManyToManyField('self', related_name="user_following", symmetrical=False)


