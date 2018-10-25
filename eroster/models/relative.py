from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel

class Relative(TimeStampedModel):
    #consultant = models.ForeignKey(Consultant)
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    international_organization = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Relative"
        verbose_name_plural = "Relatives"
  

    def __unicode__(self):
        return self.name