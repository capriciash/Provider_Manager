from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect #3
from django.http import HttpResponse #3
from itertools import chain

from . import forms
from .models import Provider #3
from .models import Driver, PASS, DefensiveDriving, Training

def dashboard(request):
    num_providers = len(Provider.objects.all())
    num_drivers = len(Driver.objects.all())
    return render(request, 'directory/dashboard.html', {'num_providers': num_providers,
                                                            'num_drivers': num_drivers})

def provider_list(request): #3
    providers = Provider.objects.all() #3
    # output = ', '.join([str(provider) for provider in providers]) #3
    # return HttpResponse(output) #3
    email = "capriciash@gmail.com"
    return render(request, 'directory/provider_list.html', {'providers': providers,
                                                            'email': email})

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'directory/driver_list.html', {'drivers': drivers})

def provider_detail(request, pk):
    # provider = Provider.objects.get(pk=pk) replaced with the 404 error line below
    provider = get_object_or_404(Provider, pk=pk)
    return render(request, 'directory/provider_detail.html', {'provider': provider})

def driver_detail(request, provider_pk, driver_pk):
    driver = get_object_or_404(Driver, provider_id=provider_pk, pk=driver_pk)
    trainings = sorted(chain(driver.pass_set.all(), driver.defensivedriving_set.all()),
                key=lambda t: t.expiration)
    return render(request, 'directory/driver_detail.html', {
            'driver': driver,
            'trainings': trainings
        })

def training_nav(request):
    return render(request, 'directory/training_nav.html')

def ddriving_list(request):
    ddrivings = DefensiveDriving.objects.all()
    return render(request, 'directory/ddriving_list.html', {'ddrivings': ddrivings})

def pass_list(request):
    passes = PASS.objects.all()
    return render(request, 'directory/pass_list.html', {'passes': passes})

# @login_required
# def provider_create(request):
#     provider = get_object_or_404(models.Provider)
#     form = forms.ProviderForm()
#     if request.method == 'POST':
#         form = form.ProviderForm(request.POST)
#         if form.is_valid():
#             provider = form.save(commmit=False)
#             #modify something first, if desired
#             provider.save()
#             messages.add_message(request, messages.SUCCESS, "Provider added!")
#             return HttpResponseRedirect(provider.get_absolute_url())
#     return render(request, 'directory/provider_form.html', {'form': form})

@login_required
def add_driver(request, provider_pk):
    provider = get_object_or_404(Provider, pk=provider_pk)
    form = forms.DriverForm()

    if request.method == 'POST':
        form = form.DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commmit=False)
            driver.provider = provider
            driver.save()
            messages.add_message(request, messages.SUCCESS, "Driver added!")
            return HttpResponseRedirect(driver.get_absolute_url())
    return render(request, 'directory/add_driver.html', {'form': form, 'provider':provider})

# def training_detail(request, driver_pk, training_pk):
#     driver = get_object_or_404(Driver, provider_id=provider_pk, pk=driver_pk)
#     trainings = sorted(chain(PASS_set.all(), DefensiveDriving_set.all()),
#                 key = lambda t: t.expiration)
#     return render(request, 'directory/driver_detail.html', {
#             'driver': driver,
#             'trainings': trainings
#             })
