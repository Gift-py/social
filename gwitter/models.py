from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __repr__(self):
        return f'{self.user.username}'

    def __str__(self):
        return f'{self.user.username}'
