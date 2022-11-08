from django.db import models
from django.utils.html import format_html



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media',null=True, blank=True)
  
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    search_fields = ['title']
    list_filter = ['title']


    def show_image_pic(self):
        if self.image:
            return format_html('<img src="%s" height="50px">' % self.image.url)
        return ('NULL')
    show_image_pic.allow_tags = True


    def _str_(self):
        return self.title


class Messenger(models.Model):
    title_messenger=models.CharField(max_length=60)
    image_messenger=models.ImageField(upload_to='media')
    
   
    

    def show_image_messenger(self):
        if self.image_messenger:
            return format_html('<img src="%s" height ="50px">' % self.image_messenger.url)
        return 'NULL'
    show_image_messenger.allow_tags=True

    def _str_(self):
        return self.title

 

