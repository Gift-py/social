from django.urls import path
from .views import dashboard, profile_list, profile, create_account, login, logout

app_name = 'gwitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile-list/', profile_list, name='profile-list'),
    path('profile/<str:username>', profile, name='profile'),
    path('create-account/', create_account, name='create-account'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
