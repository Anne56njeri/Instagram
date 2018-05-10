from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['name','Bio','profile_image']
