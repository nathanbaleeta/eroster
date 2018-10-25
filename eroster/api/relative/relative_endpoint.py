from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models.relative import Relative

class RelativeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Relative
        fields = '__all__'

class RelativeViewSet(ModelViewSet):
    queryset = Relative.objects.all()
    serializer_class = RelativeSerialiser


relativeRouter = DefaultRouter()
relativeRouter.register(r'relatives', RelativeViewSet)
