from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from login_system import settings, send_mail

# Create your views here.


def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']

        if User.objects.filter(username=username):
            messages.error(request, "Username Already Exists")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email Already Registered")
            return redirect('home')

        if len(username)>10:
            messages.error(request, "Username must be less than 10 characters")

        if password != confirmpass:
            messages.error(request, "Passwords Do Not Match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        messages.success(request, 'Your Account has been successfully created')


        #Welcome Email

        subject = "Welcome to Django Login"
        message = "Hello" + myuser.first_name + "! \n Welcome to Django! Please confirm your email!"

        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently = True)


        return redirect('signin')
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, "authentication/index.html", {'fname':fname})

        else:
            messages.error(request, "Error! Try Again!")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')