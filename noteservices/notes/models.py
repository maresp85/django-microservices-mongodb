from djongo import models
import datetime


class Notes(models.Model):
    iduser = models.IntegerField(null=False)
    title = models.CharField(null=False, max_length=100)
    body = models.CharField(null=False, max_length=240)
    register = models.DateTimeField(default=datetime.datetime.now())
