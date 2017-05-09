from django.db import models
from django.core.urlresolvers import reverse


class Rusers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    pump_name = models.CharField(max_length=1000)
    pump_status = models.BooleanField(default=False)
    def __str__(self):
        return self.pump_name+""+ str(self.pump_status)

    def get_absolute_url(self):
        return reverse('home')

