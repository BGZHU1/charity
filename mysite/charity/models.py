# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Volunteers(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number_hours = models.FloatField()
    charity_name = models.CharField(max_length=100)
    message = models.CharField(max_length = 10000)


#user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    charity_list = models.CharField(max_length=100, default='Volunteers_Home')
    number_hours = models.FloatField(default=0)


    # other fields...
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
