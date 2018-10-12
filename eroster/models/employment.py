from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Employment(TimeStampedModel):
    class Meta:
        ordering = ['-ending_date']
    #consultant = models.ForeignKey(Consultant)
    employer = models.CharField(max_length=100)
    employer_address = models.CharField(max_length=100)
    business_type = models.CharField(max_length=25)
    supervisor_name = models.CharField(max_length=45, blank=True, null=True)
    exact_job_title_held = models.CharField(max_length=45)
    no_of_employees_supervised = models.PositiveIntegerField(blank=True, null=True)
    kind_of_employees_supervised = models.CharField(max_length=25, blank=True, null=True)
    reason_for_leaving = models.CharField(max_length=100, blank=True, null=True)
    desc_of_duties = models.TextField(blank=False, null=False)
    starting_date = models.DateField(null=False)
    ending_date = models.DateField(null=False)
    annual_salary_starting = models.DecimalField(max_digits=9, decimal_places=0)
    annual_salary_final = models.DecimalField(max_digits=9, decimal_places=0)
  
    def __unicode__(self):
        return self.employer