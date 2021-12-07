from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City, Street, Shop
from .serializers import (CityListSerializer, CityDetailSerializer,
                          StreetListSerializer, ShopListSerializer,
                          ShopCreateSerializer, ShopDetailSerializer)

class CityListView(APIView):
    """Вывод списка городов"""

    def get(self, request):
        cities = City.objects.all()
        serializer = CityListSerializer(cities, many=True)
        return Response(serializer.data)


class CityDetailView(APIView):
    """Вывод конкретного города"""

    def get(self, request, pk):
        city = City.objects.get(id=pk)
        serializer = CityDetailSerializer(city)
        print(serializer.data)
        return Response(serializer.data)


class StreetListView(APIView):
    """Вывод списка улиц"""

    def get(self, request):
        streets = Street.objects.all()
        serializer = StreetListSerializer(streets, many=True)
        return Response(serializer.data)


class ShopListView(APIView):
    """Вывод списка магазинов"""

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopListSerializer(shops, many=True)
        return Response(serializer.data)


class ShopCreateView(APIView):
    """Создание магазина"""

    def post(self, request):
        shop = ShopCreateSerializer(data=request.data)
        if shop.is_valid():
            shop = shop.save()
        data = {'shop_id' : shop.id}
        return Response(status=201, data=data)


class ShopDetailView(APIView):
    """Вывод конкретного магазина"""

    def get(self, request, pk):
        shop = Shop.objects.get(id=pk)
        serializer = ShopDetailSerializer(shop)
        print(serializer.data)
        return Response(serializer.data)

    # def post(self, request):
    #     shop = ShopCreateSerializer(data=request.data)
    #     if shop.is_valid():
    #         shop.save()
    #     data = {'id' : shop.pk}
    #     return Response(status=201, data=data)