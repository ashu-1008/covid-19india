import json
import urllib
from urllib.request import urlopen

from django.shortcuts import HttpResponse, render


# Create your views here.

# confirmed
# active
# recovered
# deceased

def homeView(request):
    jsonUrl = 'https://api.covid19india.org/data.json'

    response = urlopen(jsonUrl)
    webData = json.load(response)
    data = []
    # for a in range(0, len(webData["statewise"])):
    #     b = {
    #         'confirmed': a['confirmed'],
    #         'active': a['deaths']
    #     }
    return render(request, 'home/index.html', {'dataStatewise': webData["statewise"]})
