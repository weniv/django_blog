from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import CustomUserCreationForm

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect("blog:post_list")
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("blog:post_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required(login_url="accounts:login")
def logout(request):

    if request.user.is_authenticated:
        auth_logout(request)
        
    return redirect("accounts:login")



def signup(request):
    if request.user.is_authenticated:
        return redirect("blog:post_list")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})
