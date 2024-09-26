from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)