from django.contrib.auth.models import User, Group
from rest_framework import viewsets,serializers

from .models import Mechanic, Service, ShopInventory


class ShopInventorySerializer(serializers.ModelSerializer):
    '''
    shop inventory serializer
    '''
    class Meta:
        model=ShopInventory
        fields=['name_of_part','price_of_part','car_make','car_model']

class ServiceSerializer(serializers.ModelSerializer):
    '''
    services serializers
    '''
    class Meta:
        model = Service
        fields = ['complexity', 'title', 'duration']

class MechanicSerializer(serializers.ModelSerializer):
    '''

    mechanic serializer
    '''
    services = ServiceSerializer(many=True)

    class Meta:
        model = Mechanic
        fields = ['mechanic_name', 'garage_name','services']

    def create(self, validated_data):
        services_data = validated_data.pop('services')
        mechanic = Mechanic.objects.create(**validated_data)
        for service_data in services_data:
            Service.objects.create(mechanic=mechanic, **service_data)
        return mechanic