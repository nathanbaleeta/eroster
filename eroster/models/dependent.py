from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Dependent(TimeStampedModel):
    class Meta:
        ordering = ['-birthdate']
    #consultant = models.ForeignKey(Consultant)
    name = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    relationship = models.CharField(max_length=20, blank=True, null=True)
    
    def __unicode__(self):
        return self.name