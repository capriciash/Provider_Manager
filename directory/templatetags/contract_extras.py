##Create our own custom template tags
from django import template
from directory.models import Contract, Provider

register = template.Library()

@register.simple_tag #decorator
def newest_contract():
    ''' Gets the most recent contract for the provider. '''
    return Contract.objects.latest('end_date').end_date

# Long way to register the tag
# register.simple_tag(newest_contract)

@register.inclusion_tag('directory/provider_nav.html')
def nav_providers_list():
    ''' Returns a dictionary of providers to display in the navigation pane. '''
    providers = Provider.objects.all()
    return {'providers': providers}

@register.filter("format_as_phone")
def format_as_phone(phone_number):
    ''' Takes a 10 string phone number and formats it correctly. '''
    num = str(phone_number)
    formatted = "({}) {}-{}".format(num[0:3], num[3:6], num[6:])
    return formatted
