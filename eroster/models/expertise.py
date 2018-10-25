from django.db import models
from django_extensions.db.models import TimeStampedModel

class Expertise(models.Model):
    class Meta:
        ordering = ['field']
    field = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertise"
  
    
    def __unicode__(self):
        return self.field