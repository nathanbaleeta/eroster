from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Publication


class PublicationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerialiser


publicationRouter = DefaultRouter()
publicationRouter.register(r'publications', PublicationViewSet)
