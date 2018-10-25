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

    class Meta:
        verbose_name = "Dependent"
        verbose_name_plural = "Dependents"

    def __unicode__(self):
        return '%s %s' % (self.name, self.relationship)    