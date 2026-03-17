from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("book_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})

def register_view(request):
    # HTTP POST REQUEST
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #user save in DB
            form.save()
            return redirect("login")
    else:
        # HTTP GET REQUEST
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("book_list")
