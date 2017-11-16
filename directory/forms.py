from django import forms

from . import models

class ProviderForm(forms.ModelForm):
    class Meta:
        model = models.Provider
        fields = [
            'business_name',
            'address',
            'phone_number',
            'business_license',
            'notes'
        ]

class DriverForm(forms.ModelForm):
    class Meta:
        model = models.Driver
        fields = [
            'first_name',
            'last_name',
            'driver_id',
            'birth_date',
            'hire_date',
            'license',
            'notes'
        ]
