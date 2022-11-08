from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dashboard/', login_required(views.home, login_url='/'),name='dashboard'),
    path('signUp/', views.signUp, name='signUp_page'),
    path('', views.Login, name='Login_page'),
    path('hod/', views.hod, name='hod'),
    path('active/', views.active, name='active'),



    path('addUser/',views.signUpForm, name='addUser_page'),
    path('UseUser/',views.LoginForm, name='useUser_page'),
    path('logOut/',views.logOut, name='logOut'),

]