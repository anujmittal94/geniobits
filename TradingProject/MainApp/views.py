import mimetypes
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import CsvFile, JsonFile
import json
import csv
from django.core.files.base import ContentFile
import os


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = CsvFile(file=request.FILES['file'])
            instance.save()
            handle_uploaded_file(request.FILES['file'])
            url = os.path.join(settings.MEDIA_URL, 'jsons', 'test.json')
            return render(request, 'MainApp/download.html', {'url': url})
        print(form.errors)
        return HttpResponse('<h1>File Submission Failed</h1>')
    else:
        form = UploadFileForm()
        return render(request, 'MainApp/index.html', {'form': form})


def handle_uploaded_file(file):
    candle_list = load_list(file)
    result = get_json(candle_list)
    f = ContentFile(result)
    instance = JsonFile()
    instance.file.save('test.json', f, save=True)


class Candle:
    def __init__(self, open, low, high, close, date):
        self.open = open
        self.low = low
        self.high = high
        self.close = close
        self.date = date


def load_list(file):
    candle_list = []
    file_data = file.read().decode("utf-8")
    lines = file_data.splitlines()
    reader = csv.DictReader(lines)
    for row in reader:
        candle_list.append(
            Candle(row['OPEN'], float(row['LOW']), float(row['HIGH']), row['CLOSE'], row['DATE']))
    return candle_list


def get_json(candle_list):
    result = {}
    result['open'] = candle_list[0].open
    result['close'] = candle_list[-1].close
    result['date'] = candle_list[0].date
    low = candle_list[0].low
    high = candle_list[0].high
    for candle in candle_list:
        if candle.low < low:
            low = candle.low
        if candle.high > high:
            high = candle.high
    result['low'] = str(low)
    result['high'] = str(high)
    return json.dumps(result)
