from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render

import json
import requests

def get_call(request, kwargs):
    headers = {"Host": "apim-dev-hackathon-06.azure-api.net",
                    "Ocp-Apim-Subscription-Key": settings.APIKEY,
                    "Ocp-Apim-Trace":"true"}
    url = "https://apim-dev-hackathon-06.azure-api.net/api/api/Product/%s" % (kwargs["eanCode"])
    res = {}
    if request.method == "GET":
        res = requests.get(url, headers=headers).json()
    return res

def prod_view(request, eanCode):
    product = get_call(request, {"eanCode": eanCode})
    return render(request, "prods/base.html", {"product": product})
    #return HttpResponse(json.dumps(product))
