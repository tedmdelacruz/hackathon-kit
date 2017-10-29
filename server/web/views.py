from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib import auth
from django.conf import settings

from api.serializers import UserSerializer


def app(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'web/app.html')


def index(request):
    if request.user.is_authenticated:
        return redirect('app')
    return render(request, 'web/index.html', {'project_name': settings.PROJECT_NAME})


def login(request):
    if request.method != 'POST':
        return render(request, 'web/login.html', {'project_name': settings.PROJECT_NAME})

    data = request.POST
    user = auth.authenticate(username=data['username'], password=data['password'])

    if not user:
        messages.add_message(request, messages.ERROR,
                             'Invalid username or password')
        return redirect('index')

    auth.login(request, user)
    return redirect('app')


def register(request):
    if request.method != 'POST':
        return render(request, 'web/register.html', {'project_name': settings.PROJECT_NAME})

    serializer = UserSerializer(data=request.POST)
    if not serializer.is_valid():
        messages.add_message(request, messages.ERROR, 'Invalid registration. Please try again.')
        return redirect('register')

    serializer.save()
    messages.add_message(request, messages.INFO, 'Successfully registered. Please login to continue.')
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('index')
