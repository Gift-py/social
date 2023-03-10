from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __repr__(self):
        return f'{self.user.username}'

    def __str__(self):
        return f'{self.user.username}'

class Gweet(models.Model):
    user = models.ForeignKey(User, related_name='gweets', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'{self.user} '
            f'({self.created_at:%Y-%m-%d %H:%M}): '
            f'{self.body[:30]}...'
        )

    def __repr__(self):
        return (
            f'{self.user} '
            f'({self.created_at:%Y-%m-%d %H:%M}): '
            f'{self.body[:30]}...'
        )