from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Gweet

# Register your models here.
admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(User, UserAdmin)
admin.site.register(Gweet)
