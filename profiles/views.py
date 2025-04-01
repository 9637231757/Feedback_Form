"""from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
from .forms import ProfileForm
# Create your views here.

def store_files(file):
    with open("temp/image.jpg","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
            
          
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form":form
        })

    def post(self, request):
        submited_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")
        
        return render(request, "profiles/create_profile.html", {
            "form":submitted_form
        })"""
        
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ProfileForm
from .models import UserProfile

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")
        
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })        
        
