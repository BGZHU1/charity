# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.template import loader
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .form import *

from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .serializer import ProfileSerializer

class PersonalView(ObtainAuthToken):

    #overwrite the post method inside ObtainAuthToken
    def post(self, request, *args, **kwargs):
        print(request.POST)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        #this part will check able to generate token or not/ raise exception if not able to login and generate token

        if not serializer.is_valid(raise_exception=False) :
            template = loader.get_template('registration/login.html')
            context = {
                'login_failed': 'login failed, please try again'
            }
            return HttpResponse(template.render(context, request))

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print('token', token)
        print(self.schema) # from parent class
        #return Response({'token': token.key})



        #this may be different view later
        #get personal page info
        #will first login for future update info
        print(request)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)


        profile = models.Profile.objects.get(username=user)
        print(profile)
        message_list = models.Message.objects.filter(user=user).values()
        print(message_list, 'message list')
        template = loader.get_template('personal_page.html')
        context = {
            'volunteer_name': profile.first_name,
            'volunteer_hours': profile.number_hours,
            'volunteer_moneny_value': float(profile.number_hours) * 23,
            'message_list': message_list,
            'percentage_volunteer_hours': float(profile.number_hours) / 200 * 100
        }
        return HttpResponse(template.render(context, request))


'''
#this will potentailly be the class after got the token for react front end -- not used at this moment
class UserVerificationView(APIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)

    #this means require authentication first
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        print(request.POST)
        content = {
            'user': request.POST['user'],  # `django.contrib.auth.User` instance.
            'auth':None,  # None
        }
        return Response(content)


'''


# Create your views here.
#@login_required
'''
def personal(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    # use user to retrieve unique datap
    print(request.user, request.user.is_authenticated)
    if request.user.is_authenticated == False:
        return HttpResponseRedirect('/')

    print(request)
    profile = models.Profile.objects.get(username = request.user)
    print(profile)
    message_list = models.Message.objects.filter(user = request.user).values()
    print(message_list,'message list')
    template = loader.get_template('personal_page.html')
    context = {
    'volunteer_name': profile.first_name,
    'volunteer_hours':profile.number_hours,
    'volunteer_moneny_value' : float(profile.number_hours) * 23,
    'message_list' : message_list,
    'percentage_volunteer_hours' : float(profile.number_hours) / 200 * 100
    }
    return HttpResponse(template.render(context, request))

#render view for login -- or get to

def user_login(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    """
    List all code snippets, or create a new snippet.
    """
    print('user login')
    if request.method == 'GET':
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
     
        #profile = Profile()
        return render(request, "login.html")


    elif request.method == 'POST':
        #add authentication here
        user_login = request.POST
        print(user_login)
        email = user_login['email']
        password = user_login['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            #need change to retrieve data page, now just redirect to home
            #from user, get first name
            login(request, user)
            firstname = user.first_name
            #print(firstname)
            return redirect('/personal/' + firstname)
            #return personal(request, firstname, user)
        else:
            template = loader.get_template('login.html')
            context = {
                'login_failed' : 'login failed, please try again'
            }
            return HttpResponse(template.render(context, request))

'''
class CreateUserView(CreateAPIView):

    model = Profile
    #template_name = 'registration/login.html'

    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = ProfileSerializer

    #ovewrite the post method for redirect
    def post(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs) #first get results from super methods
        return HttpResponseRedirect('/')






'''
def register(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    #figure out how to create new user and authentication
    if request.method == 'POST':
        #need to validate form information here

        user_info = request.POST
        print(user_info)
        firstname = user_info['firstname']
        lastname = user_info['lastname']
        email = user_info['email_address']
        password = user_info['password']
        password2 = user_info['password2']
        #charity = user_info['charity_name']
        if password != password2 :
            template = loader.get_template('user_register.html')
            context = {
                'user_creation_failed' : 'please enter the same password twice'
            }
            return HttpResponse(template.render(context, request))

        charity = ''
        print(user_info)
        print('form', UserRegistrationForm(request.POST).is_valid())

        user = None
        try :

            #user = User.objects.create_user(username = email, password = password,  first_name = firstname, last_name = lastname)
            #user.save()
            #some how need to validate form
            if UserRegistrationForm(request.POST).is_valid():
                profile = models.Profile.objects.create(username = email, first_name = firstname, last_name = lastname, charity_list =charity, number_hours = 0)
                profile.set_password(password)
                #profile = models.Profile.objects.create(user=user, charity_list =charity, number_hours = 0, firstname = firstname, lastname = lastname)
                profile.save()

        except :
            template = loader.get_template('user_register.html')
            context = {
                'user_creation_failed' : 'the email already exists, please use an different email and try again'
            }
            return HttpResponse(template.render(context, request))


        #return render(request, "user_register.html", {"form": user_profile})


        return HttpResponseRedirect('/user/login/')
    else:
        profile = Profile()
        return render(request, "user_register.html", {"form": profile})


'''



def update_hours(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')

    if request.method == 'POST':
        print(request.POST)
        hours = request.POST['hour']


        #generate auto message on board

        #first get hours in Profile
        profile = models.Profile.objects.get(username=request.user)

        try :
            print(request.user)
            profile = models.Profile.objects.get(username = request.user)
            firstname = profile.first_name
            new_total_hours = profile.number_hours + float(hours)
            profile.number_hours = new_total_hours
            print(profile.number_hours, new_total_hours)
            profile.save()

            #pop up share screen
            #first creat additaionl entry
            #user = models.ForeignKey(User, on_delete=models.CASCADE)
            organization = request.POST['organization']
            hours = request.POST['hour']
            date = request.POST['date']
            message = models.Message.objects.create(user = request.user, organization =organization, hours = hours, date = date)
            message.save()
        except :
            return HttpResponse('error input, please double check the hours and charity organization')


    #render the content again
    profile = models.Profile.objects.get(username=request.user)
    print(profile)
    message_list = models.Message.objects.filter(user=request.user).values()
    print(message_list, 'message list')
    template = loader.get_template('personal_page.html')
    context = {
        'volunteer_name': profile.first_name,
        'volunteer_hours': profile.number_hours,
        'volunteer_moneny_value': float(profile.number_hours) * 23,
        'message_list': message_list,
        'percentage_volunteer_hours': float(profile.number_hours) / 200 * 100
    }
    return HttpResponse(template.render(context, request))
  
def delete_journal(request, id) :
    profile = models.Profile.objects.get(username = request.user)
    message_to_delete = models.Message.objects.get(pk=id)
    hours = message_to_delete.hours
    message_to_delete.delete()

    #update total hours
    new_total_hours = profile.number_hours - float(hours)
    profile.number_hours = new_total_hours
    print(profile.number_hours, new_total_hours)
    profile.save()

    #delete individual entry

    # render the content again
    profile = models.Profile.objects.get(username=request.user)
    print(profile)
    message_list = models.Message.objects.filter(user=request.user).values()
    print(message_list, 'message list')
    template = loader.get_template('personal_page.html')
    context = {
        'volunteer_name': profile.first_name,
        'volunteer_hours': profile.number_hours,
        'volunteer_moneny_value': float(profile.number_hours) * 23,
        'message_list': message_list,
        'percentage_volunteer_hours': float(profile.number_hours) / 200 * 100
    }
    return HttpResponse(template.render(context, request))