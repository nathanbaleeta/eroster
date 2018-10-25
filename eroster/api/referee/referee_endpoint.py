from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Referee

class RefereeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'

class RefereeViewSet(ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerialiser


refereeRouter = DefaultRouter()
refereeRouter.register(r'referees', RefereeViewSet)
