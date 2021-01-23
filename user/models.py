from django.db import models


class Userapp(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
