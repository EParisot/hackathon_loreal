# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request, product):
    return HttpResponse("Product %s" % product)
