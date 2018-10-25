from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from eroster.models import Clerical


class ClericalSerialiser(serializers.ModelSerializer):
	
	class Meta:
		model = Clerical
		fields = ('id', 'language', 'typing_shorthand')

class ClericalViewSet(ModelViewSet):
    queryset = Clerical.objects.all()
    serializer_class = ClericalSerialiser
    permission_class = [DjangoModelPermissions]


clericalRouter = DefaultRouter()
clericalRouter.register(r'clericals', ClericalViewSet)
