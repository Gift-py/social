from django.shortcuts import render, redirect
from .models import User, Gweet
from .forms import GweetForm, UserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout


def create_account(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST':
        if request.user.is_anonymous:
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                
                return redirect('gwitter:dashboard')
            else:
                print(form.errors)

    return render(request, 'gwitter/create_account.html', {'form':form, 'activate':False})

def login(request):
    
    if request.method == 'POST':
        if request.user.is_anonymous:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('gwitter:dashboard')
        else:
            print('There is a logged in user')
    return render(request, 'gwitter/login.html', {'activate':False})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('gwitter:login')

def dashboard(request):

    form = GweetForm(request.POST or None)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if form.is_valid():
                gweet = form.save(commit=False)
                gweet.user = User.objects.get(username=request.user.username)
                gweet.save()
                return redirect('gwitter:dashboard')
    
    gweets = Gweet.objects.all().order_by('-created_at')
    return render(request, 'gwitter/dashboard.html', {'gweets':gweets, 'form':form, 'activate':True})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = User.objects.exclude(username=request.user.username)
        return render(request, 'gwitter/profile_list.html', {'profiles':profiles, 'activate':True})


def profile(request, username):
    follow_option = False
    if request.user.is_authenticated:        
        profile = User.objects.get(username=username)

        current_user_profile = User.objects.get(username=request.user.username)
        data = request.POST
        action = data.get('follow')

        if profile != current_user_profile:
            if action == 'follow':
                current_user_profile.follows.add(profile)
            elif action == 'unfollow':
                current_user_profile.follows.remove(profile)
            follow_option = True
        
            current_user_profile.save()

        user_follows = profile in User.objects.get(username=request.user.username).follows.all()
    
        return render(request, 'gwitter/profile.html', 
                {'profile':profile, 'followers':len(profile.followed_by.all()), 
                'follows':len(profile.follows.all()), 'user_follows':user_follows, 'activate':True, 'follow_option':follow_option})
