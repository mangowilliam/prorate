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
        fields = ['title','image','description','link','ratings','profile']