from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Education


class EducationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerialiser


educationRouter = DefaultRouter()
educationRouter.register(r'education', EducationViewSet)
