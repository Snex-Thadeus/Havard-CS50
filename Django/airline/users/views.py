from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "users/user.html")
    
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {"message": "Invalid Credentials!"}
            return render(request, "users/login.html", context=context)
            
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    context =  {"message": "Logged Out"}
    return render(request, "users/login.html", context=context)