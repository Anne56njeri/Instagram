from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    Bio= models.TextField()
    profile_image=models.ImageField(upload_to = 'profiles/',blank=True)
    user=models.ForeignKey(User)
