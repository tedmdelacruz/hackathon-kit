from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.decorators import api_view


def app(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'web/app.html')


def landing(request):
    if request.user.is_authenticated:
        return redirect('app')
    return render(request, 'web/landing.html')


@api_view(['POST'])
def signin(request):
    data = request.POST
    user = authenticate(username=data['username'], password=data['password'])

    if not user:
        messages.add_message(request, messages.ERROR,
                             'Invalid username or password')
        return render(request, 'web/landing.html')

    login(request, user)
    return redirect('app')


def signout(request):
    logout(request)
    return redirect('landing')
