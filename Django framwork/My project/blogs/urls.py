from django.urls import path
from. import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('home/', login_required(views.home,login_url='/log'), name='home_page'),
    path('messenger/',login_required(views.messenger,login_url='/log'), name='messenger_page'),
    path('profile/',login_required(views.profile,login_url='/log'), name='profile_page'),
    path('setting/',login_required(views.setting, login_url='/log'),name='setting_page'),
    path('log/',views.log,name='log_page'),
    path('signup/',views.signup, name='signup_page'),
    path('',views.before, name='before_page'),
    
  # url system
    path('addUser/', views.signUpForm, name='addUser'),
    path('useUser/', views.loginForm, name='useUser'),
    path('logOut/', views.logOut, name='logOut'),

]


