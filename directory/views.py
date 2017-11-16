from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect #3
from django.http import HttpResponse #3
from itertools import chain

from . import forms
from .models import Provider #3
from .models import Driver, PASS, DefensiveDriving, Training, FirstAidCPR

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

def provider_detail(request, provider_pk):
    # provider = Provider.objects.get(pk=pk) replaced with the 404 error line below
    provider = get_object_or_404(Provider, pk=provider_pk)
    return render(request, 'directory/provider_detail.html', {'provider': provider})

def driver_detail(request, provider_pk, driver_pk):
    driver = get_object_or_404(Driver, pk=driver_pk)
    trainings = sorted(chain(driver.pass_set.all(), driver.defensivedriving_set.all()),
                key=lambda t: t.expiration)
    return render(request, 'directory/driver_detail.html', {
            'driver': driver,
            'trainings': trainings
        })

    def get_absolute_url(self):
        return reverse('directory/driver/detail.html', kwargs={'provider_pk': self.provider.pk, 'driver_pk': self.pk})

def training_nav(request):
    return render(request, 'directory/training_nav.html')

def ddriving_list(request):
    ddrivings = DefensiveDriving.objects.all()
    return render(request, 'directory/ddriving_list.html', {'ddrivings': ddrivings})

def pass_list(request):
    passes = PASS.objects.all()
    return render(request, 'directory/pass_list.html', {'passes': passes})

def firstaid_list(request):
    faids = FirstAidCPR.objects.all()
    return render(request, 'directory/firstaid_list.html', {'faids': faids})

def user_profile(request):
    return render(request, 'directory/user_profile.html')

def login(request):
    return render(request, 'directory/login.html')



@login_required
def add_driver(request):
    # provider = get_object_or_404(Provider, pk=provider_pk)
    form = forms.DriverForm()

    if request.method == 'POST':
        form = forms.DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            # driver.provider = provider
            driver.save()
            messages.add_message(request, messages.SUCCESS, "Driver added!")
            return HttpResponseRedirect(driver.get_absolute_url())
    return render(request, 'directory/driver_form.html', {'form': form})

@login_required
def add_provider(request):
    form = forms.ProviderForm()

    if request.method == 'POST':
        form = forms.ProviderForm(request.POST)
        if form.is_valid():
            provider = form.save()
            messages.add_message(request, messages.SUCCESS, "Provider added!")
            return HttpResponseRedirect(provider.get_absolute_url())
    return render(request, 'directory/provider_form.html', {'form': form})

@login_required
def edit_provider(request, provider_pk):
    provider = get_object_or_404(Provider, pk=provider_pk)
    form = forms.ProviderForm(instance=provider)

    if request.method == 'POST':
        form = forms.ProviderForm(instance=provider, data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Updated {}".format(form.cleaned_data['business_name']))
            return HttpResponseRedirect(provider.get_absolute_url())
    return render(request, 'directory/provider_form.html', {'form': form})

@login_required
def edit_driver(request, provider_pk, driver_pk):
    driver = get_object_or_404(Driver, pk=driver_pk, provider_id=provider_pk)
    form = forms.DriverForm(instance=driver)

    if request.method == 'POST':
        form = forms.DriverForm(instance=driver, data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Updated {} {}".format(form.cleaned_data['first_name'], form.cleaned_data['last_name']))
            return HttpResponseRedirect(driver.get_absolute_url())
    return render(request, 'directory/driver_form.html', {'form': form})

# def training_detail(request, driver_pk, training_pk):
#     driver = get_object_or_404(Driver, provider_id=provider_pk, pk=driver_pk)
#     trainings = sorted(chain(PASS_set.all(), DefensiveDriving_set.all()),
#                 key = lambda t: t.expiration)
#     return render(request, 'directory/driver_detail.html', {
#             'driver': driver,
#             'trainings': trainings
#             })
