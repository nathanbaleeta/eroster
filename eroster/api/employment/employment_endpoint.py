from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Employment

class EmploymentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'

class EmploymentViewSet(ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerialiser


employmentRouter = DefaultRouter()
employmentRouter.register(r'employment', EmploymentViewSet)
