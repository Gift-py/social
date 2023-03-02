from django.urls import path
from .views import dashboard, profile_list, profile

app_name = 'gwitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile-list/', profile_list, name='profile-list'),
    path('profile/<str:username>', profile, name='profile'),
]
