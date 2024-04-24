from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class RepairTable(models.Model):
    userID = models.IntegerField()
    equipment= models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    fault = models.CharField(max_length=128)
    contact = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    unit = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)
    state = models.CharField(max_length=32)

class SupportTable(models.Model):
    userID = models.IntegerField()
    date= models.CharField(max_length=64)
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    thing = models.CharField(max_length=128)
    contact = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    unit = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
