from django import forms
from .models import Profile,Image
from django.contrib.auth.forms import UserChangeForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name','Bio','profile_image']
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields = ['name','image_caption','image_path']
