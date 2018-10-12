from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Expertise


class ExpertiseSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'

class ExpertiseViewSet(ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerialiser


expertiseRouter = DefaultRouter()
expertiseRouter.register(r'expertise', ExpertiseViewSet)
