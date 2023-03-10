from django import forms
from .models import Profile, User, Gweet
from django.contrib.auth.forms import UserCreationForm

class GweetForm(forms.ModelForm):
    body = forms.CharField(required=True, 
                           widget=forms.widgets.Textarea(
                                attrs={
                                    "placeholder": "Gweet something...",
                                    "class": "textarea is-success is-medium",
                                }
                            ),
                            label='',)

    class Meta():
        model = Gweet
        exclude = ('user', )


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
