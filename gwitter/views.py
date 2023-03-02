from django.shortcuts import render
from .models import Profile, User


def dashboard(request):
    return render(request, 'base.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'gwitter/profile_list.html', {'profiles':profiles})

def profile(request, username):
    profile = Profile.objects.get(user=User.objects.get(username=username))

    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')

        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        
        current_user_profile.save()

    user_follows = profile in request.user.profile.follows.all()
    
    return render(request, 'gwitter/profile.html', 
                  {'profile':profile, 'followers':len(profile.followed_by.all()), 
                   'follows':len(profile.follows.all()), 'user_follows':user_follows})