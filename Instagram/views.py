from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ImageForm,SignUpForm,UserForm
from .models import Profile,Image
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import login,authenticate
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.name=form.cleaned_data.get('name')
            user.profile.Bio=form.cleaned_data.get('Bio')
            user.profile.profile_image=form.cleaned_data.get('profile_image')
            user.save()
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request, user)

    else:
        form=SignUpForm()
    return render (request,'signup.html',{'form':form})
@login_required(login_url='/accounts/login')
def home(request):
    title='Welcome to Instaphoto'
    return render(request,'main/home.html',{"title":title})
@login_required(login_url='/accounts/login')
def index(request):
    title='Welcome to instagram'
    profile_info =UserProfile.objects.all()
    images_prof=Image.objects.all()
    return render(request,'main/index.html',{"title":title,"profile_info":profile_info,"images_prof":images_prof})
@login_required
def first_profile(request,profile_id):
    try:
        profile_info =Profile.objects.get(id=profile_id)
    except DoesNotExsist:
        raise Http404()

    return render(request,'main/profile.html',{"profile_info":profile_info})

def add_image(request):
   current_profile=Profile.objects.get(user=request.user)
   if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form_details=form.save(commit=False)
            form_details.profile=current_profile
            form_details.save()
            return redirect(index)
   else:
        form=ImageForm()

   return render(request,'main/image.html',{"form":form})
def details(request,image_id):
    try:
        image_details = Image.objects.get(id=image_id)
    except DoesNotExsist:
        raise Http404()
    return render(request,'main/details.html',{"image_details":image_details})

def search_profile(request):
    search_term=request.GET.get("profile")
    searched_profiles=Profile.search(search_term)
    return render (request,'main/search.html',{"searched_profiles":searched_profiles})
def second_profile(request):
    profile_details=Profile.objects.all()
    return render(request,'main/home.html',{"profile_info":profile_info})
