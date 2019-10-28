from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.


def get_signup(request):
    "This get the sign up page"
    return render(request, 'signup.html')


def get_login(request):
    "This get the log in page"
    return render(request, 'login.html')


def post_login(request):
    "This is post log in data"
    auth.logout(request)

    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/index')
    else:
        return redirect('/login')


def post_logout(request):
    "Post loguout function"
    auth.logout(request)
    return redirect('/index')
