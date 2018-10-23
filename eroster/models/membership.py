from django.db import models
from django_extensions.db.models import TimeStampedModel

class Membership(TimeStampedModel):
	#consultant = models.ForeignKey(Consultant)
    society = models.CharField(max_length=100)
    activities = models.TextField(blank=False, null=False)
  
    def __unicode__(self):
        return self.society