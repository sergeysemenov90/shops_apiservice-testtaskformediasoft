from rest_framework import serializers
from shops.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    """Список городов"""

    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'