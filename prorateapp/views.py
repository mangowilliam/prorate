from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm
from . models import Project
# Create your views here.


def home(request):
    projects=Project.get_projects()
    return render(request, 'home.html',{"projects":projects})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 
def search_project(request):
    
    if 'projects' in request.GET and request.GET["projects"]:
        repos = request.GET.get("projects")
        searched_projects = Project.search_project(repos)
        print(searched_projects)
        message = f"{repos}"

        return render(request, 'search.html', {"message": message, "project": searched_projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html', {"message": message})