# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Volunteers, Profile

admin.site.register(Volunteers)
admin.site.register(Profile)
