from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

# Create your models here.

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(to=User)
    name = models.CharField(max_length=64)
    is_locked = models.BooleanField()
    auto_lock_after = models.DateTimeField()

class TimeSlot(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(to=Schedule)
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    auto_lock_after = models.DateTimeField()
    is_locked = models.BooleanField()
    reservation_limit = models.IntegerField()

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    time_slot = models.ForeignKey(to=TimeSlot)
    email = models.EmailField()
    # TODO: Find out how to store phone numbers
    #phone = models.PhoneNumberField()
    comment = models.CharField(max_length=256)
