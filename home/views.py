import json
from urllib.request import urlopen

from django.shortcuts import HttpResponse, render

# Create your views here.


def homeView(request):
    jsonUrl = 'https://api.covid19india.org/data.json'                              # url for stateWise data
    stateData = json.load(urlopen(jsonUrl))

    jsonUrl2 = 'https://api.covid19india.org/v2/state_district_wise.json'           # url for districtWise data
    districtData = json.load(urlopen(jsonUrl2))

    data_for_frontend = {
        'dataStateWise': stateData["statewise"],
        'dataDistrictWise': districtData,
    }
    return render(request, 'home/index.html', data_for_frontend)
