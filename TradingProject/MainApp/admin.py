from django.contrib import admin
from .models import CsvFile, JsonFile

# admin.site.register(Candle)
admin.site.register(CsvFile)
admin.site.register(JsonFile)
