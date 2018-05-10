from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    Bio= models.TextField()
    user=models.ForeignKey(User)
