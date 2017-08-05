from django.db import models

# Create your models here.
class Provider(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=56)
    contract = models.FileField(upload_to='provider_contracts')
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    address = models.CharField(max_length=56)
    phone_number = models.IntegerField()
    business_license = models.CharField(max_length=18)
    date_added = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return self.business_name

class Driver(models.Model):
    company = models.ForeignKey('Provider')
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    driver_id = models.CharField(max_length=12)
    birth_date = models.DateField()
    hire_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    eligible = models.BooleanField(default=False)
    # license = models.CharField(max_length=12)
    # back_check = models.CharField(max_length=12)
    # training1 = ...
    # training2 = ...

class Provider_Contact(models.Model):
    company = models.ForeignKey('Provider')
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    title = models.CharField(max_length=56)
    phone_number = models.IntegerField()
    email_address = models.EmailField()

# class Pass_Training(models.Model):
#     driver = models.ForeignKey()
#     training_date = models.DateField()
#     time_since = models.DurationField()
#     cert_file = models.FileField(upload_to='PASS_certificates')
