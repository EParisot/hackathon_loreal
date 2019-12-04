from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import requests
#user_code = "2CBFB2C5A90835F8AA6A98A02C964A99"

reco = [None, None, None]

with open("media/products.json") as f:
    prods = json.load(f)

def get_reco():
    global reco
    reco = [None, None, None]
    for prod in prods:
        if prods[prod]["subAxisName"] == "FACE MAKEUP":
            reco[0] = prod
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "EYE MAKEUP":
            reco[1] = prod
            break
    for prod in prods:
        if prods[prod]["subAxisName"] == "LIP MAKEUP":
            reco[2] = prod
            break
    return reco

def recommendations(request, user):
    reco = get_reco()
    return HttpResponse(json.dumps(reco))

def new_prod(request, idx):
    global reco
    if idx < len(reco) and reco[idx] != "" and reco[idx] != None:
        subAxisName = prods[reco[idx]]["subAxisName"]
        for prod in prods:
            if prods[prod]["subAxisName"] == subAxisName and prod != reco[idx]:
                reco[idx] = prod
    return HttpResponse(json.dumps(reco))

def index(request):
    return HttpResponse("App index")
