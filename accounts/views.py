from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError

def login_view(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid Username or credentials! Please check and try again."

    return render(request, 'login.html', {'error_message': error_message})

def signup_view(request):
    error_message = ""
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        except IntegrityError:
            error_message = "User already exists."

    return render(request, 'signup.html',  {'error_message': error_message})
