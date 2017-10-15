from django.contrib import admin
from .models import Provider, Driver, Provider_Contact, Contract

class DriverInline(admin.TabularInline):
    model = Driver

class ContractInline(admin.TabularInline):
    model = Contract

class ProviderAdmin(admin.ModelAdmin):
    inlines = [
        DriverInline,
        ContractInline
    ]

# Register your models here.
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Driver)
admin.site.register(Provider_Contact)
# admin.site.register(Background_Check)
