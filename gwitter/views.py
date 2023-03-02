from django.shortcuts import render
from .models import Profile, User


def dashboard(request):
    return render(request, 'base.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'gwitter/profile_list.html', {'profiles':profiles})

def profile(request, username):
    profile = Profile.objects.get(user=User.objects.get(username=username))
    return render(request, 'gwitter/profile.html', {'profile':profile})