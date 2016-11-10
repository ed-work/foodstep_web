from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField
from taggit.managers import TaggableManager


class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='recipes')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(blank=True, null=True, max_length=5)
    img = VersatileImageField(upload_to='recipes/')
    public = models.BooleanField(default=True)

    favorites = models.ManyToManyField(User, related_name='favorites',
                                       blank=True)
    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def is_favorited(self, user):
        return user.id in self.favorites.values_list('id', flat=True)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=50)


class Step(models.Model):
    recipe = models.ForeignKey(Recipe)
    text = models.TextField(blank=True, null=True)
    img = VersatileImageField(upload_to='recipes/')
