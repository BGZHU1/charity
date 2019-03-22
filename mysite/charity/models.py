# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.
class Message(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, default='deargoodpeople')
    hours = models.FloatField(default=0)
    date = models.CharField(max_length=100, default=datetime.datetime.today().strftime('%Y-%m-%d'))





#user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    charity_list = models.CharField(max_length=100, default='Volunteers_Home')
    number_hours = models.FloatField(default=0)
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')


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
