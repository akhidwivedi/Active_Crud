from django.db import models
from datetime import datetime
from django.utils.timezone import now


# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    DOB = models.DateTimeField(default=now,blank=True)
    location =  models.CharField(max_length=50)




    def __str__(self):
        return self.email
