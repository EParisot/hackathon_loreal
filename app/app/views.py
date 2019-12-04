from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import requests

#user_code = "2CBFB2C5A90835F8AA6A98A02C964A99"

reco = None

def get_prods():
    with open("media/products.json") as f:
        prods = json.load(f)
    global reco
    reco = {}
    for prod in prods:
        if prods[prod]["subAxisName"] == "FACE MAKEUP":
            reco[prod] = prods[prod]
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "EYE MAKEUP":
            reco[prod] = prods[prod]
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "LIP MAKEUP":
            reco[prod] = prods[prod]
            break
    return reco

def recommendations(request, user):
    reco = get_prods()
    return HttpResponse(json.dumps(reco))

def new_prod(request, subAxisName, eanCode):
    global reco
    with open("media/products.json") as f:
        data = json.load(f)
        for prod in data:
            if data[prod]["subAxisName"] == subAxisName and prod != eanCode:
                reco[eanCode] = data[prod]
    return HttpResponse(json.dumps(reco))

def index(request):
    return HttpResponse("App index")
