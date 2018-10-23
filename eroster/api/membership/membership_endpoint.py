from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from eroster.models import Membership


class MembershipSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerialiser


membershipRouter = DefaultRouter()
membershipRouter.register(r'membership', MembershipViewSet)
