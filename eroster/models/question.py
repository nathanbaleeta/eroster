from django.db import models
from django_extensions.db.models import TimeStampedModel

class Question(TimeStampedModel):
	ANSWERS = (
        ('YES', 'Yes'),
        ('NO', 'No'),
    )
	#consultant = models.ForeignKey(Consultant)
    description = models.TextField(blank=False, null=False)
    response = models.CharField(max_length=3, blank=True, choices=ANSWERS)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
  
  
    def __unicode__(self):
        return self.description