from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

class all_pincodes(models.Model):
    Country_Code = models.CharField(max_length=245, null = True)
    Postal_Code = models.CharField(max_length=245, null = True)
    Place_Name = models.CharField(max_length=245, null = True)
    State_Name = models.CharField(max_length=245, null = True)
    District_Name_or_City_Name = models.CharField(max_length=245, null = True)
    extra_District_Name_or_City_Name = models.CharField(max_length=245, null = True)
    latitude = models.CharField(max_length=245, null = True)
    longitude = models.CharField(max_length=245, null = True)


class country_content(models.Model):
    Country_Code = models.CharField(max_length=245, null = True)
    Long_Content = models.TextField()
