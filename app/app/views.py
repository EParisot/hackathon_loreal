from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import requests
#user_code = "2CBFB2C5A90835F8AA6A98A02C964A99"

reco = []

def get_prods():
    with open("media/products.json") as f:
        prods = json.load(f)
    global reco
    reco = []
    for prod in prods:
        if prods[prod]["subAxisName"] == "FACE MAKEUP":
            reco.append(prods[prod])
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "EYE MAKEUP":
            reco.append(prods[prod])
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "LIP MAKEUP":
            reco.append(prods[prod])
            break
    return reco

def recommendations(request, user):
    reco = get_prods()
    return HttpResponse(reco)

def new_prod(request, idx):
    global reco
    subAxisName = reco[idx]["subAxisName"]
    productName = reco[idx]["productName"]
    with open("media/products.json") as f:
        prods = json.load(f)
    for prod in prods:
        if prods[prod]["subAxisName"] == subAxisName and prods[prod] != productName:
            reco[idx] = prods[prod]
    return HttpResponse(reco)

def index(request):
    return HttpResponse("App index")
