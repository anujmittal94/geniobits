from django.forms import ModelForm
from .models import CsvFile


class UploadFileForm(ModelForm):
    class Meta:
        model = CsvFile
        fields = ['file']
