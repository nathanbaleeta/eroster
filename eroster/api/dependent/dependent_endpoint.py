from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Dependent

class DependentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Dependent
        fields = '__all__'

class DependentViewSet(ModelViewSet):
    queryset = Dependent.objects.all()
    serializer_class = DependentSerialiser


dependentRouter = DefaultRouter()
dependentRouter.register(r'dependents', DependentViewSet)
