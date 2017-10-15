from django import forms

class ReportIssueForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    issue = forms.CharField(widget=forms.Textarea)

    #then create a view, a url route, and a template
