from django.conf import settings
from django.db import models


class CsvFile(models.Model):
    file = models.FileField(upload_to='csvs/', null=True, blank=True)


# class Candle(models.Model):
#     open = models.FloatField()
#     low = models.FloatField()
#     high = models.FloatField()
#     close = models.FloatField()
#     date = models.DateTimeField()


class JsonFile(models.Model):
    file = models.FileField(upload_to='jsons/')
