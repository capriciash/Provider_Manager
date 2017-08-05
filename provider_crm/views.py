from django.http import HttpResponse #1

def project_intro(request): #1
    return HttpResponse('This is the base site for the Provider CRM project!') #1
