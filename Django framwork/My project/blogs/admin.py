from django.contrib import admin
from .models import Blog,Messenger

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'show_image_pic']

# Register your models here.
admin.site.register(Blog,BlogAdmin)

class Messenger_admin(admin.ModelAdmin):
    list_display=['title_messenger','show_image_messenger']

admin.site.register(Messenger,Messenger_admin)




