from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ImageForm
from .models import Profile
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    title='Welcome to instagram'
    profile_info =Profile.objects.all()
    images_prof=Images.objects.all()
    return render(request,'main/index.html',{"title":title,"profile_info":profile_info,"images_prof":images_prof})
def first_profile(request):
    current_user=request.user
    user=Profile.objects.get(user_id=current_user)
    if request.method == 'POST':
        form =ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            first_profile=form.save(commit=False)
            first_profile.user=current_user
            first_profile.save()
            return redirect(index)
    else:
        form = ProfileForm()


    return render(request,'main/profile.html',{"form":form})
def add_image(request):
    if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    return render(request,'main/image.html',{"form":form})
