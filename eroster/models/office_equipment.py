from django.db import models
from django_extensions.db.models import TimeStampedModel


class OfficeEquipment(TimeStampedModel):
    office_machine = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.office_machine