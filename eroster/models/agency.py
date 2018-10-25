from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField


class Agency(TimeStampedModel):
    name = models.CharField(max_length=50)
    country = CountryField(blank_label='(select country)')

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"
  
    def __unicode__(self):
        return '%s %s' % (self.name, self.country)    