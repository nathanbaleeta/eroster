from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Contact


class ContactSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser


contactRouter = DefaultRouter()
contactRouter.register(r'contacts', ContactViewSet)
