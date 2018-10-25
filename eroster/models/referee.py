from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel

class Referee(TimeStampedModel):
    #consultant = models.ForeignKey(Consultant)
    full_name = models.CharField(max_length=50)
    full_address = models.CharField(max_length=100)
    email = models.EmailField()
    business_or_occupation = models.CharField(max_length=45)

    class Meta:
        verbose_name = "Referee"
        verbose_name_plural = "Referees"
  
  
    def __unicode__(self):
        return self.full_name