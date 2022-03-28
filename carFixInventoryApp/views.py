from django.shortcuts import render

from carFixInventoryApp.models import Mechanic, Service,  ShopInventory

from .serializers import MechanicSerializer, ServiceSerializer,ShopInventorySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
class InventorySnippetList(generics.ListCreateAPIView):
    '''
    used generic view for shorter code with all the functionalities combined
    list create called in one function
    '''
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer


class InventorySnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    used generic view for shorter code with all the functionalities combined
    retrieve update called in one function
    '''
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer




class MechanicViewSet(viewsets.ModelViewSet):
    # '''view for mechanics used viewset to separate post and get
    # viewset offers shorter code compared to function methods
    # '''
    serializer_class=MechanicSerializer

    def get_queryset(self):
        mechanic=Mechanic.objects.all()
        return mechanic


class ServiceViewSet(viewsets.ModelViewSet):
    # '''view for mechanics used viewset to separate post and get
    # viewset offers shorter code compared to function methods
    # '''
    serializer_class=ServiceSerializer

    def get_queryset(self):
        service=Service.objects.all()
        return service
