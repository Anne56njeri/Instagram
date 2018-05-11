from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    Bio= models.TextField()
    profile_image=models.ImageField(upload_to = 'profiles/',blank=True)
    user=models.ForeignKey(User)
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


class Image(models.Model):
    name=models.CharField(max_length=20)
    image_caption=models.CharField(max_length=1000,blank=True)
    profile=models.ForeignKey(Profile,null=True)
    image_path=models.ImageField(upload_to='images/',blank=True)
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()    
