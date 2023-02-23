from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __repr__(self):
        return f'{self.user.username}'

    def __str__(self):
        return f'{self.user.username}'


#using signals to crate a new profile anytime a user is created
@receiver(post_save, sender=User) #linking the create profile function and the create user function
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        print('\n\n',instance.profile,'\n\n')
        user_profile.follows.add(instance.profile.id)
        user_profile.save()
        



