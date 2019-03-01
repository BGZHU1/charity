# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.template import loader
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


#from models import Volunteers

# Create your views here.
def homepage(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    volunteer_list = models.Volunteers.objects.get(pk=1)
    print(volunteer_list)
    template = loader.get_template('homepage.html')
    context = {
    'volunteer_list': volunteer_list
    }
    return HttpResponse(template.render(context, request))

#render view for login -- or get to
def login(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
        '''
        volunteer_list = models.Volunteers.objects.get(pk=1)
        print(volunteer_list)
        template = loader.get_template('login.html')
        context = {
        'volunteer_list': volunteer_list,
        'form' : Profile()
        }
        return HttpResponse(template.render(context, request))
        #snippets = Snippet.objects.all()
            #serializer = SnippetSerializer(snippets, many=True)
        #return JsonResponse(serializer.data, safe=False)
        '''
        #profile = Profile()
        return render(request, "login.html")


    elif request.method == 'POST':
        #add authentication here
        user_login = request.POST
        print(user_login)
        username = user_login['username']
        password = user_login['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            #need change to retrieve data page, now just redirect to home
            return HttpResponseRedirect('/')
        else:
            template = loader.get_template('login.html')
            context = {
                'login_failed' : 'login failed, please try again'
            }
            return HttpResponse(template.render(context, request))



def register(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    #figure out how to create new user and authentication
    if request.method == 'POST':
        user_info = request.POST
        username = user_info['user_name']
        email = user_info['email_address']
        password = user_info['password']
        print(user_info)
        user = User.objects.create_user(username, email, password)
        user.save()

        #profile potentially for additional user information
        profile = models.Profile.objects.create(user=user, charity_list ='ABC', number_hours = 10)
        profile.save()



        #return render(request, "user_register.html", {"form": user_profile})


        return HttpResponseRedirect('/login/')
    else:
        profile = Profile()
        return render(request, "user_register.html", {"form": profile})
