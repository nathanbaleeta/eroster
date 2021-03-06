from django.db import models
from django_extensions.db.models import TimeStampedModel
from languages.fields import LanguageField


class Clerical(TimeStampedModel):
    #office_equipment_used = models.TextField()
    language = LanguageField(blank=True)
    typing_shorthand = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = "Clerical"
        verbose_name_plural = "Clericals"
  
    
    def __unicode__(self):
        return '%s %s' % (self.language, self.typing_shorthand)    