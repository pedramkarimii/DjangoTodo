from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.db import IntegrityError
from django.http import HttpResponseNotFound, HttpResponse

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                User.objects.create_user(cd['username'], cd['email'], cd['password'])
                messages.success(request, 'Registered successfully', 'success')
                return HttpResponse(status=200)  
            except IntegrityError:
                messages.error(request, 'Username or email already exists', 'danger')
                return HttpResponseNotFound('User registration failed. Please try again.', status=404)
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully', 'success')
                return redirect('home')
            else:

                messages.error(request, 'Invalid username or password', 'danger')
                return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_login.html', {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully', 'success')
    return redirect('home')
