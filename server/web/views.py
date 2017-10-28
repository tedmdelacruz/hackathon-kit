from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


def app(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'web/app.html')


def index(request):
    if request.user.is_authenticated:
        return redirect('app')
    return render(request, 'web/index.html', {'project_name': settings.PROJECT_NAME})


def signin(request):
    if request.method != 'POST':
        return render(request, 'web/login.html', {'project_name': settings.PROJECT_NAME})

    data = request.POST
    user = authenticate(username=data['username'], password=data['password'])

    if not user:
        messages.add_message(request, messages.ERROR,
                             'Invalid username or password')
        return redirect('index')

    login(request, user)
    return redirect('app')


def signout(request):
    logout(request)
    return redirect('index')
