from django import forms
from .models import Profile,Image
from django.contrib.auth.forms import UserChangeForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name','Bio','profile_image']
class ImageForm(forms.ModelForm):
    model=Image
    fields = ['name','caption','image_path']
