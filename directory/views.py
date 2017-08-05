from django.shortcuts import render
from django.http import HttpResponse #3

from .models import Provider #3

def provider_list(request): #3
    providers = Provider.objects.all() #3
    output = ', '.join([str(provider) for provider in providers]) #3
    return HttpResponse(output) #3
