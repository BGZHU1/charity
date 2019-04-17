# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Message, Profile
#from .form import UserRegistrationForm, UserChangeForm

from django.contrib.auth.admin import UserAdmin

admin.site.register(Message)

admin.site.register(Profile)
'''
class ProfileUserAdmin(UserAdmin):
    add_form = UserChangeForm
    form = UserRegistrationForm
    model = Profile
    #list_display = ['username', 'charity_list', 'number_hours','first_name', 'last_name']
admin.site.register(Profile, ProfileUserAdmin)
'''
