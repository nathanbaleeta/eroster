from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name','last_name', 'date_joined','is_admin','is_active')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerialiser


userRouter = DefaultRouter()
userRouter.register(r'user', UserViewSet)
