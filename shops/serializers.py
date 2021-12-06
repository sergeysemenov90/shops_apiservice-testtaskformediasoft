from rest_framework import serializers
from shops.models import City, Street, Shop


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'