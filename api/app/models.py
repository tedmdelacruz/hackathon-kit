from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    avatar_url = models.TextField()
    status = models.BooleanField(default=True)
