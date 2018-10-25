from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField


class Education(TimeStampedModel):
    class Meta:
        ordering = ['-attended_to']

    QUALIFICATION_TYPE = (
        ('', 'Select Qualification Type'),
        ('High School', 'HIGH SCHOOL'),
        ('Certificate', 'CERTIFICATE'),
        ('Diploma', 'DIPLOMA'),
        ('Bachelors', 'BACHELORS'),
        ('Masters', 'MASTERS'),
        ('PhD', 'PHD'),
    )
    
    #consultant = models.ForeignKey(Consultant)
    institution = models.CharField(max_length=200)
    place = models.CharField(max_length=50)
    country = CountryField(blank_label='(select country)')
    attended_from = models.DateField(null=False)
    attended_to = models.DateField(null=False)
    qualiification_type = models.CharField(max_length=20, choices=QUALIFICATION_TYPE,)
    qualiification_obtained = models.CharField(max_length=150, blank=True)
    academic_distinction_obtained = models.CharField(max_length=100, blank=True)
    main_course_of_study = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
  

    def __unicode__(self):
        return self.institution

   
    
    
    
  
