from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from eroster.models import Agency


class AgencySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerialiser
    permission_class = [DjangoModelPermissions]


agencyRouter = DefaultRouter()
agencyRouter.register(r'agency', AgencyViewSet)
