from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)


class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(to=City, related_name='street', related_query_name='streets', on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    street = models.ForeignKey(to=Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=30)
    opening_time = models.TimeField()
    closing_time = models.TimeField()