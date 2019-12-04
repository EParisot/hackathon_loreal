from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import requests

APIKEY = "8d1038b7c5c34c5b8da987d21323b700"
NBPROD = 4
#user_code = "2CBFB2C5A90835F8AA6A98A02C964A99"

def get_call(request, kwargs):
    headers = {"Host": "apim-dev-hackathon-06.azure-api.net",
                    "Ocp-Apim-Subscription-Key":APIKEY,
                    "Ocp-Apim-Trace":"true"}
    url = "https://apim-dev-hackathon-06.azure-api.net/apireco/recommend/consumer:%s:%d" % (kwargs["user"], NBPROD)
    recommendations = {}
    if request.method == "GET":
        for product_code in requests.get(url, headers=headers).json():
            product_url = "https://apim-dev-hackathon-06.azure-api.net/apireco/product:%s" % (product_code)
            recommendations[str(product_code)] = requests.get(product_url, headers=headers).json()
    return recommendations 

class Recommendation(APIView):
    def get(self, request, *args, **kwargs):
        recommendations = get_call(request, kwargs)
        return Response(recommendations)

def new_prod(request, subAxisName, eanCode):
    with open("media/prod_types.json") as f:
        data = json.load(f)
    for prod in data[subAxisName]:
        if prod != eanCode:
            return HttpResponse(prod)

def index(request):
    return HttpResponse("App index")
