from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from building.forms import SignupForm, LoginForm
from building.models import Building, Entrance


def index(request):
    buildings = Building.objects.all()

    return render(request, "index.html", {"buildings": buildings})


def entrance(request, pk):
    entrance_door = Entrance.objects.get(pk=pk)

    return render(request, "entrance.html", {"entrance": entrance_door})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("building:index"))

