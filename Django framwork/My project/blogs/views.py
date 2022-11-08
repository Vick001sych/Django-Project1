from django.shortcuts import render, redirect
from .models import Blog, Messenger 
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.

def home(request):
    news = Blog.objects.all().order_by('-pk')
    return render(request, 'index2/indexxxx.html', {
    'news': news
    })
   
def messenger(request):
    
    mess=Messenger.objects.all()
    return render(request, 'index2/messenger.html',{
        'mess' : mess,
        
    })

def c(request):
    return render(request, 'index2/c.html')
def a(request):
    return render(request, 'index2/a.html')
def select(request):
    return render(request, 'index2/select.html')

def profile(request):
    return render(request, 'index2/profile.html')
def setting(request):
    return render(request, 'index2/setting.html')
def log(request):
    return render(request, 'index1/log.html')
def signup(request):
    return render(request, 'index1/signup.html')
def before(request):
    return render(request, 'index1/before.html')


# System's functions
def signUpForm(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['Repeatpassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
           
            messages.info(request, 'This username is already exist!')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            
            messages.info(request, 'This email is already exist!')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            user.save()
            return redirect('/log')
    else:
        messages.info(request, 'The password do not match!')
        return redirect('/signup')

def loginForm(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/home')
    else:
        messages.info(request,'Not found :(')
        return redirect('/log')

def logOut(request):
    auth.logout(request)
    return redirect('/')

