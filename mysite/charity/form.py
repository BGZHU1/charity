from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Profile(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())
    charity_name = forms.CharField(initial=None)
    number_hours = forms.FloatField()

    '''
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
    '''
