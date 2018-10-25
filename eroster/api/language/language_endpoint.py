from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from eroster.models import Language


class LanguageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerialiser
    permission_class = [DjangoModelPermissions, ]


languageRouter = DefaultRouter()
languageRouter.register(r'languages', LanguageViewSet)
