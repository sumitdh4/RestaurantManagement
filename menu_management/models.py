from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    discount = models.FloatField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    items = models.ManyToManyField(Items)
    type = models.CharField(max_length=100, default="Veg")

    def __str__(self):
        return self.type
