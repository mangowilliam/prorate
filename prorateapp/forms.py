from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project,Profile

class UserRegistrationForm(UserCreationForm):
    email =forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AddProjectForm(forms.ModelForm):
     class Meta:
        model = Project
        exclude = ['pub_date']
        
class UserUpdateForm(forms.ModelForm):
    email =forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']