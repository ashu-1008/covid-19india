import json
from urllib.request import urlopen

from django.shortcuts import HttpResponse, render

# Create your views here.


def homeView(request):
    jsonUrl = 'https://api.covid19india.org/data.json'                              # url for stateWise data
    stateData = json.load(urlopen(jsonUrl))

    jsonUrl2 = 'https://api.covid19india.org/v2/state_district_wise.json'           # url for districtWise data
    districtData = json.load(urlopen(jsonUrl2))
    stateOrderWise = []

    def myFunc(e):                                                                  # func to sort state cases in
        return int(e['confirmed'])                                                  # decreasing order
    stateData["statewise"].sort(reverse=True, key=myFunc)

    for oneData in districtData:
        oneData["districtData"].sort(reverse=True, key=myFunc)
    data_for_frontend = {
        'dataStateWise': stateData["statewise"],
        'dataDistrictWise': districtData,
    }
    return render(request, 'home/index.html', data_for_frontend)
