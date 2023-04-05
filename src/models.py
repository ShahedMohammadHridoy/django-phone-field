from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = PhoneNumberField()
