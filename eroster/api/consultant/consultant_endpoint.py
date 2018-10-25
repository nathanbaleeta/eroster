from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Consultant


class ConsultantSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = '__all__'


class ConsultantViewSet(ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerialiser


consultantRouter = DefaultRouter()
consultantRouter.register(r'consultants', ConsultantViewSet)
