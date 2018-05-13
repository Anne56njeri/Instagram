from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=30)
    Bio= models.TextField()
    profile_image=models.ImageField(upload_to = 'profiles/',blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    @classmethod
    def search(cls,search_term):
        profiles=cls.objects.filter(name__icontains=search_term)
        return profiles

#one image can belong to various profiles
class Image(models.Model):
    name=models.CharField(max_length=20)
    image_caption=models.CharField(max_length=1000,blank=True)
    image_path=models.ImageField(upload_to='images/',blank=True)
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
