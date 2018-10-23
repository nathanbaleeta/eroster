from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from eroster.models import OfficeEquipment


class OfficeEquipmentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = OfficeEquipment
        fields = '__all__'


class OfficeEquipmentViewSet(ModelViewSet):
    queryset = OfficeEquipment.objects.all()
    serializer_class = OfficeEquipmentSerialiser
    permission_class = [DjangoModelPermissions]

office_equipmentRouter = DefaultRouter()
office_equipmentRouter.register(r'office-equipment', OfficeEquipmentViewSet)
