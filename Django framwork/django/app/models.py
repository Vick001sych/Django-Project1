from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'Active'),
        )
    user_type = models.CharField(choices=USER, default=1, max_length=50)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Active(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
   