from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #3

from .models import Provider #3
from .models import Driver

def provider_list(request): #3
    providers = Provider.objects.all() #3
    # output = ', '.join([str(provider) for provider in providers]) #3
    # return HttpResponse(output) #3
    email = "capriciash@gmail.com"
    return render(request, 'directory/provider_list.html', {'providers': providers,
                                                            'email': email})

def provider_detail(request, pk):
    # provider = Provider.objects.get(pk=pk) replaced with the 404 error line below
    provider = get_object_or_404(Provider, pk=pk)
    return render(request, 'directory/provider_detail.html', {'provider': provider})

def driver_detail(request, provider_pk, driver_pk):
    driver = get_object_or_404(Driver, provider_id=provider_pk, pk=driver_pk)
    return render(request, 'directory/driver_detail.html', {'driver': driver})
