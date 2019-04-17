from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

'''
class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Profile
        fields = ('username', 'password', 'charity_list', 'number_hours')

class UserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = ('username', 'password','charity_list', 'number_hours')
'''

class UserRegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    email_address = forms.EmailField()
