from django.db import models
from django_extensions.db.models import TimeStampedModel
from languages.fields import LanguageField


class Language(TimeStampedModel):
    PROFICIENCY = (
        ('NONE', 'None'),
        ('BASIC', 'Basic'),
        ('INTERMEDIATE', 'Intermediate'),
        ('PROFICIENT', 'Proficient'),
        ('FLUENT', 'Fluent'),
    )
    
    language = LanguageField(blank=True)
    speaking_proficiency = models.CharField(max_length=13, choices=PROFICIENCY)
    reading_proficiency = models.CharField(max_length=13, choices=PROFICIENCY)
    writing_proficiency = models.CharField(max_length=13, choices=PROFICIENCY)
    mother_tongue = models.BooleanField(blank=True)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
  
    
    def __unicode__(self):
        return self.language