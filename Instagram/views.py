from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    title='Welcome to instagram'
    return render(request,'main/index.html',{"title":title})
def first_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=current_user
            profile.save()
    else:
        form = ProfileForm()        


    return render(request,'main/profile.html',{"form":form})
