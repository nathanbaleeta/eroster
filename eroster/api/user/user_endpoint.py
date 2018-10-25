from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email', 'first_name','last_name', 'date_joined','is_active','groups','is_staff')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_class = (DjangoModelPermissions)


userRouter = DefaultRouter()
userRouter.register(r'users', UserViewSet)

