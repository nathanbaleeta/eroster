from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from eroster.api.user.user_endpoint import userRouter
from eroster.api.agency.agency_endpoint import agencyRouter
from eroster.api.contact.contact_endpoint import contactRouter
from eroster.api.employment.employment_endpoint import employmentRouter
from eroster.api.dependent.dependent_endpoint import dependentRouter
from eroster.api.relative.relative_endpoint import relativeRouter
from eroster.api.referee.referee_endpoint import refereeRouter
from eroster.api.expertise.expertise_endpoint import expertiseRouter
from eroster.api.publication.publication_endpoint import publicationRouter
from eroster.api.consultant.consultant_endpoint import consultantRouter
from eroster.api.membership.membership_endpoint import membershipRouter
from eroster.api.education.education_endpoint import educationRouter
from eroster.api.language.language_endpoint import languageRouter
from eroster.api.clerical.clerical_endpoint import clericalRouter
from eroster.api.office_equipment.office_equipment_endpoint import office_equipmentRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(userRouter.urls)),
    url(r'^api/', include(agencyRouter.urls)),
    url(r'^api/', include(contactRouter.urls)),
    url(r'^api/', include(employmentRouter.urls)),
    url(r'^api/', include(dependentRouter.urls)),
    url(r'^api/', include(relativeRouter.urls)),
    url(r'^api/', include(refereeRouter.urls)),
    url(r'^api/', include(expertiseRouter.urls)),
    url(r'^api/', include(publicationRouter.urls)),
    url(r'^api/', include(consultantRouter.urls)),
    url(r'^api/', include(membershipRouter.urls)),
    url(r'^api/', include(educationRouter.urls)),
    url(r'^api/', include(languageRouter.urls)),
    url(r'^api/', include(clericalRouter.urls)),
    url(r'^api/', include(office_equipmentRouter.urls)),
    


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
