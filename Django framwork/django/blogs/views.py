from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from app.models import CustomUser,Active
# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'signUp.html')
def Login(request):
    return render(request, 'Login.html')

def hod(request):
    return render(request, 'view_hod.html')
def active(request):
    return render(request, 'view_active.html')

#Authenticate

def addUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']

    if password == re_password:
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'This username is already exists!')
            return redirect('/signUp')
        elif CustomUser.objects.filter(email = email).exists():
            messages.info(request, 'This email is already exists!')
            return redirect('/signUp')
        else:
            
            new_user = CustomUser(
            username = username,
            email = email,
            password = password,
            user_type = 2,
            )
        new_user.save()
       
        return redirect('/')
    else:
        messages.info(request, 'The password do not match!')
        return redirect('/signUp')

def LoginForm(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        
        if user.user_type== 1:
            return HttpRespon('This is Hod Panel')
        if user.user_type== 2:
            return HttpRespon('This is Active Panel')
        # return redirect('/dashboard')
    else:
        messages.error(request, 'Not Found :(')
        return redirect('/')

def logOut(request):
    auth.logout(request)
    return redirect('/')


def signUpForm(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']
    

    if password == re_password:
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'This username is already exists!')
            return redirect('/signUp')
        elif CustomUser.objects.filter(email = email).exists():
            messages.info(request, 'This email is already exists!')
            return redirect('/signUp')
        else:
            
            new_user = CustomUser.objects.create_user(
            username = username,
            email = email,
            password = password,
            user_type = 2,
            )
            new_user.save()
        return redirect('/')
    else:
        messages.info(request, 'The password do not match!')
        return redirect('/signUp')

def LoginForm(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        user_type = user.user_type
        if user_type== '1':
            return redirect('/hod')
        if user_type== '2':
            return redirect('/dashboard')
       
    else:
        messages.error(request, 'Not Found :(')
        return redirect('/')

def logOut(request):
    auth.logout(request)
    return redirect('/')