from django.db import models
from django_extensions.db.models import TimeStampedModel


class OfficeEquipment(TimeStampedModel):
    office_machine = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Office Equipment"
        verbose_name_plural = "Office Equipment"
  
    
    def __unicode__(self):
        return self.office_machine