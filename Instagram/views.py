from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    title='Welcome to instagram'
    profile_info =Profile.objects.all()
    return render(request,'main/index.html',{"title":title,"profile_info":profile_info})
def first_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form =ProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=current_user
            profile.save()
            return redirect(index)
    else:
        form = ProfileForm()


    return render(request,'main/profile.html',{"form":form})
