# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Volunteers(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number_hours = models.FloatField()
    charity_name = models.CharField(max_length=100)
    message = models.CharField(max_length = 10000)
