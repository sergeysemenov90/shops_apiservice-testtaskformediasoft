from django.shortcuts import render
from rest_framework import viewsets
from shops.models import City, Street, Shop
from shops.serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewset(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopViewset(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

# Create your views here.
