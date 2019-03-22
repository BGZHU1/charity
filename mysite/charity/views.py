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



#from models import Volunteers



# Create your views here.
def personal(request, firstname) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')
    # use user to retrieve unique datap
    print(request.user)
    if request.user.is_authenticated == False:
        return HttpResponseRedirect('/user_login/')


    profile = models.Profile.objects.get(user = request.user)
    message_list = models.Message.objects.filter(user = request.user).values()
    print(message_list,'message list')
    template = loader.get_template('personal_page.html')
    context = {
    'volunteer_name': profile.firstname,
    'volunteer_hours':profile.number_hours,
    'volunteer_moneny_value' : float(profile.number_hours) * 23,
    'message_list' : message_list,
    'percentage_volunteer_hours' : float(profile.number_hours) / 2000
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
        email = user_login['email']
        password = user_login['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            #need change to retrieve data page, now just redirect to home
            #from user, get first name
            print(user, 'get user')
            login(request, user)
            firstname = models.Profile.objects.get(user = request.user).firstname
            #print(firstname)
            return redirect('/personal/' + firstname)
            #return personal(request, firstname, user)
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
        print(user_info)
        firstname = user_info['firstname']
        lastname = user_info['lastname']
        email = user_info['email_address']
        password = user_info['password']
        #charity = user_info['charity_name']
        charity = ''
        print(user_info)
        user = User.objects.create_user(username = email, password = password,  first_name = firstname, last_name = lastname)
        user.save()

        #profile potentially for additional user information
        profile = models.Profile.objects.create(user=user, charity_list =charity, number_hours = 0, firstname = firstname, lastname = lastname)
        profile.save()



        #return render(request, "user_register.html", {"form": user_profile})


        return HttpResponseRedirect('/user_login/')
    else:
        profile = Profile()
        return render(request, "user_register.html", {"form": profile})

def landing(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')

    template = loader.get_template('landing_page.html')
    context = {}
    return HttpResponse(template.render(context, request))


def update_hours(request) :
    #return HttpResponse('homepage')
    #return render(request, 'homepage.html')

    if request.method == 'POST':
        print(request.POST)
        hours = request.POST['hour']


        #generate auto message on board

        #first get hours in Profile
        print(request.user)
        profile = models.Profile.objects.get(user = request.user)
        firstname = profile.firstname
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







            #need change to retrieve data page, now just redirect to home
    return HttpResponseRedirect('/personal/' + firstname)
    '''
        else:
            template = loader.get_template('personal_page.html')
            context = {
                'login_failed' : 'login failed, please try again'
            }
            return HttpResponse(template.render(context, request))
    '''
