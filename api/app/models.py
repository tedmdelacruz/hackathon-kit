from django.db import models


class User(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    name = models.CharField(max_length=64)
    username = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField()
    avatar_url = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=STATUS_ACTIVE)
