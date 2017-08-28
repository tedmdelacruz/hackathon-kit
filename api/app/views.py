from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from app.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_on')
    serializer_class = UserSerializer
