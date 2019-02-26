# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader
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
        #snippets = Snippet.objects.all()
        #serializer = SnippetSerializer(snippets, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return "hello get login"

    elif request.method == 'POST':
        '''
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        '''
        return "hello post login"

#method to get login request
