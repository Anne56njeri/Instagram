from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    title='Welcome to instagram'
    return render(request,'main/index.html',{"title":title})
def first_profile(request):
    user=User.objects.all()
    return render(request,'main/profile.html',{"user":user})
