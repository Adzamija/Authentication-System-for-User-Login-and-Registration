from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.db import IntegrityError

# Create your views here.
def index(request):
        return render(request, "users/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Checking for user in the User model
        if user is not None:
            login(request, user)
            message = False
            return HttpResponseRedirect(reverse("home"))
        else:
            message = True
            return render(request, "users/login.html", {
                "message": message
            })

    else:
        return render(request, "users/login.html")


def register(request):
    if request.method == "POST":
        # Taking POST data
        email = request.POST["username"]
        password = request.POST["password"]
        confirmation_passwrod = request.POST["confirmation"]
        # Checking password and confirmation password
        if password != confirmation_passwrod:
            return render(request, "users/register.html",{
                "message": "Password must match!"
            })
        # Try to add user in the User model
        try:
            user = User.objects.create_user(email, password)
            user.save()
        # If user name is already in the User model(if user is already registred)
        except IntegrityError:
            return render(request, "users/register.html", {
                "message": "Email is already registred."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def home(request):
    return render(request, "users/home.html")

