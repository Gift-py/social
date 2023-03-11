from django.db import models
from django.contrib.auth.models import AbstractUser, User as DjangoUser


class User(DjangoUser):
    
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    REQUIRED_FIELDS= ["first_name", "last_name"]
	
    def __repr__(self):
        return f'{self.user.username}'

    def __str__(self):
        return f'{self.user.username}'

class Gweet(models.Model):
    user = models.ForeignKey(User, related_name='user_gweets', on_delete=models.DO_NOTHING)
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
    
class Comments(models.Model):
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.DO_NOTHING)
    gweet  = models.ForeignKey(Gweet, related_name='gweet_comments', on_delete=models.CASCADE)
