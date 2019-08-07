from djongo import models
import datetime


class Users(models.Model):
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=True, max_length=100)
    age = models.IntegerField(null=True)
    gender = models.CharField(null=True, max_length=1)
    email = models.CharField(null=False, max_length=100)
    date_register = models.DateField(default=datetime.datetime.now())
