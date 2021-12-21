from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.


def auction_land(request, *args, **kwargs):
    return HttpResponse('hello form auction')