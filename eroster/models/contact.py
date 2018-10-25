from django.db import models
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class Contact(TimeStampedModel):
    #consultant = models.ForeignKey(Consultant)
    permanent_address = models.CharField(max_length=50)
    permanent_addr_tel = PhoneNumberField(default="")
    present_address = models.CharField(max_length=50,null=True, blank=True)
    present_addr_tel = PhoneNumberField(default="")
    permanent_addr_fax = models.CharField(max_length=20, null=True, blank=True)
    office_tel = PhoneNumberField(default="")
    office_fax = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField() 

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
  
        
    def __unicode__(self):
        return self.email