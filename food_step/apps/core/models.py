from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    following = models.ManyToManyField(User, related_name='following')
    follower = models.ManyToManyField(User, related_name='follower')
