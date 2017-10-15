# from django.http import HttpResponse #1
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from . import forms

def project_intro(request): #1
    # return HttpResponse('This is the base site for the Provider CRM project!') #1
    return render(request, 'home.html')

def issue_view(request):
    form = forms.ReportIssueForm()
    if request.method == 'POST':
        form = forms.ReportIssueForm(request.POST) #Get info from form
        if form.is_valid():
            send_mail(
                'Issue from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['issue'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['capriciash@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS,
            "Thanks for helping us improveo our site!")
            return HttpResponseRedirect(reverse('issue'))
    return render(request, 'issue_form.html', {'form': form})
