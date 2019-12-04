from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import requests

APIKEY = "8d1038b7c5c34c5b8da987d21323b700"
NBPROD = 4
#user_code = "2CBFB2C5A90835F8AA6A98A02C964A99"

def get_prods():
    with open("media/products.json") as f:
        prods = json.load(f)
    recommendations = {}
    for prod in prods:
        if prods[prod]["subAxisName"] == "FACE MAKEUP":
            recommendations[prod] = prods[prod]
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "EYE MAKEUP":
            recommendations[prod] = prods[prod]
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "LIP MAKEUP":
            recommendations[prod] = prods[prod]
            break
    return recommendations

class Recommendation(APIView):
    def get(self, request, *args, **kwargs):
        recommendations = get_prods()
        return Response(recommendations)

def new_prod(request, subAxisName, eanCode):
    with open("media/products.json") as f:
        data = json.load(f)
        for prod in data:
            if data[prod]["subAxisName"] == subAxisName and prod != eanCode:
                return HttpResponse(prod)

def index(request):
    return HttpResponse("App index")
