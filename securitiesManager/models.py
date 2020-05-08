from django.db import models


# Create your models here.
class Security(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)


class Index(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    securities = models.ManyToManyField(Security, default=None)


class Price(models.Model):
    security = models.ForeignKey(
        Security, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)


class Weight(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, default=1)
    security = models.ForeignKey(
        Security, on_delete=models.CASCADE, default=1)
    weight = models.FloatField()
