from django.contrib.auth import get_user_model
from django.db import models


class Building(models.Model):
    address = models.CharField(max_length=256)
    user = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.address


class Entrance(models.Model):
    number = models.PositiveIntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"Entrance number {self.number}"


class Apartment(models.Model):
    number = models.PositiveIntegerField()
    entrance = models.ForeignKey(Entrance, on_delete=models.CASCADE)

    def __str__(self):
        return f"apartment number: {self.number}"






