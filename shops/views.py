from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import City, Street, Shop
from .serializers import (CityListSerializer, CityDetailSerializer,
                          StreetListSerializer, ShopListSerializer,
                          ShopCreateSerializer, ShopDetailSerializer)
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .service import ShopsFilter
from datetime import datetime

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
        return Response(serializer.data)


class StreetListView(APIView):
    """Вывод списка улиц"""

    def get(self, request):
        streets = Street.objects.all()
        serializer = StreetListSerializer(streets, many=True)
        return Response(serializer.data)


class ShopListView(ListAPIView):
    """Вывод списка магазинов"""

    def get_queryset(self):
        queryset = Shop.objects.all()
        open = self.request.GET.get('open')
        time = datetime.now().time()
        print(time)
        if open == '1':
            print('We have open parameter')
            queryset = queryset.filter(opening_time__lte=time).filter(closing_time__gt=time)
        if open == '0':
            print('We have 0 open parameter')
            queryset = queryset.filter(Q(opening_time__gt=time) | Q(closing_time__lte=time))

        return queryset

    serializer_class = ShopListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ShopsFilter


class ShopCreateView(CreateAPIView):
    """Создание магазина"""

    serializer_class = ShopCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id': serializer.data["id"]}, status=status.HTTP_201_CREATED, headers=headers)


class ShopDetailView(APIView):
    """Вывод конкретного магазина"""

    def get(self, request, pk):
        shop = Shop.objects.get(id=pk)
        serializer = ShopDetailSerializer(shop)
        print(serializer.data)
        return Response(serializer.data)
