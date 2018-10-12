from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Consultant(TimeStampedModel):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    MARITAL_STATUS = (
        ('SINGLE', 'Single'),
        ('MARRIED', 'Married'),
        ('SEPARATED', 'Separated'),
        ('WIDOW', 'Widow'),
        ('WIDOWER', 'Widower'),
        ('DIVORCED', 'Divorced'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    #family_name = models.CharField(max_length=20)               
    #first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True) 
    maiden_name = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES,)
    birth_date = models.DateField(null=False)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    place_of_birth = models.CharField(max_length=45)
    nationality_at_birth = CountryField(blank_label='(select country)')
    present_nationality = CountryField(blank_label='(select country)')
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    #prefered_field_of_work = models.CharField(max_length=50)
    
    #def __unicode__(self):
    #    return self.family_name

