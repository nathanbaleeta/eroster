from django.db import models
from django_extensions.db.models import TimeStampedModel
from languages.fields import LanguageField


class Language(TimeStampedModel):
    language = LanguageField(blank=True)
    other = models.CharField(max_length=20, blank=True)
    
    read_easily = models.BooleanField(blank=True)
    read_not_easily = models.BooleanField(blank=True)
    write_easily = models.BooleanField(blank=True)
    write_not_easily = models.BooleanField(blank=True)
    speak_easily = models.BooleanField(blank=True)
    speak_not_easily = models.BooleanField(blank=True)
    understand_easily = models.BooleanField(blank=True)
    understand_not_easily = models.BooleanField(blank=True)
    
    mother_tongue = models.BooleanField(blank=True)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
  
    
    def __unicode__(self):
        return self.language