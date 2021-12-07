from rest_framework import serializers
from shops.models import City, Street, Shop


class CityListSerializer(serializers.ModelSerializer):
    """Список городов"""

    class Meta:
        model = City
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    """Конкретный город"""

    class Meta:
        model = City
        fields = '__all__'


class StreetListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Street
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'


class ShopDetailSerializer(serializers.ModelSerializer):
    """Конкретный магазин"""

    class Meta:
        model = Shop
        fields = '__all__'


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'