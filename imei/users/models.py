from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
	
    name = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    imei = models.CharField(max_length=300)
    imei1= models.CharField(max_length=300)
    mob_no = models.CharField(max_length=30)

def __str__(self):
        return self.imei



    
    