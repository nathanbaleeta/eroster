from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField


class Publication(models.Model):
    #consultant = models.ForeignKey(Consultant)
    title = models.CharField(max_length=200, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    date_published = models.DateField(blank=True, null=True)
    city_published = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField(blank_label='(select country)')
    
    def __unicode__(self):
        return self.title