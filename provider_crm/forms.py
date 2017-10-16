from django import forms
from django.core import validators

def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


class ReportIssueForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    issue = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput,
                                label="Leave empty",
                                # validators=[validators.MaxLengthValidator(0)], #built-in
                                validators=[must_be_empty] #custom one
                                )
#then create a view, a url route, and a template

#better to use a built in validator or custom one so that it can be reused
    # def clean_honeypot(self):
    #     honeypot = self.cleaned_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError("honeypot should be left empty.  bot alert.")
    #     return honeypot

    def clean(self): #for the whole form
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']

        if email != verify:
            raise forms.ValidationError("You need to enter the same email in both fields.")
