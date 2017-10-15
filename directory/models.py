from django.db import models

class Provider(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=56)
    address = models.CharField(max_length=56)
    phone_number = models.IntegerField(max_length=10, )
    business_license = models.CharField(max_length=18)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

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
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.DateTimeField(auto_now_add=True)
    eligible = models.BooleanField(default=False)
    license = models.CharField(max_length=12)
    notes = models.TextField(blank=True, default='')
    # back_check = models.CharField(max_length=12)
    # training1 = ...
    # training2 = ...

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

# class Pass_Training(models.Model):
#     driver = models.ForeignKey()
#     training_date = models.DateField()
#     time_since = models.DurationField()
#     cert_file = models.FileField(upload_to='PASS_certificates')
