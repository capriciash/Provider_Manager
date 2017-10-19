from django.db import models
from django.core.urlresolvers import reverse

class Provider(models.Model):
    business_name = models.CharField(max_length=56)
    address = models.CharField(max_length=56)
    phone_number = models.IntegerField()
    business_license = models.CharField(max_length=18)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

class Contract(models.Model):
    provider = models.ForeignKey(Provider)
    contract = models.FileField(upload_to='provider_contracts')
    start_date = models.DateField()
    end_date = models.DateField()

class Driver(models.Model):
    provider = models.ForeignKey(Provider)
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    driver_id = models.CharField(max_length=12)
    birth_date = models.DateField()
    hire_date = models.DateField()
    eligible = models.BooleanField(default=False)
    license = models.CharField(max_length=12)
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name', ]

class Provider_Contact(models.Model):
    company = models.ForeignKey(Provider)
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    title = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name + self.last_name

    def mailto(self):
        return '{}, {} <{}>'.format(self.first_name, self.last_name, self.email)

class Background_Check(models.Model):
    driver = models.ForeignKey(Driver)
    date_completed = models.DateField()
    date_expiring = models.DateField()
    granting_agency = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.User...

class Training(models.Model):
    driver = models.ForeignKey(Driver)
    training_date = models.DateField()
    time_since = models.DurationField()
    cert_file = models.FileField(upload_to='Training_Certificates')
    granting_agency = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True,default='')
    # created_by = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class PASS(Training):
    name = models.CharField(default="Passenger Assistance Safety and Sensitivity", max_length=255)
    expiration = models.DateField()

    def get_absolute_url(self):
        return reverse('directory:pass', kwargs={
            'driver_pk': self.driver_id,
            'pass_pk': self.id
        })

class DefensiveDriving(Training):
    name = models.CharField(default="Defensive Driving", max_length=255)
    expiration = models.DateField()

    def get_absolute_url(self):
        return reverse('directory:defensive', kwargs={
            'driver_pk': self.driver_id,
            'defensive_pk': self.id
        })

class FirstAidCPR(Training):
    name = models.CharField(default="First Aid and CPR", max_length=255)
    expiration = models.DateField()

    def get_absolute_url(self):
        return reverse('directory:firstaidcpr', kwargs={
            'driver_pk': self.driver_id,
            'firstaidcpr': self.id
        })
