import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def GekoAPI_getStatus(request):
    response= requests.get('https://api.coingecko.com/api/v3/ping')

    return HttpResponse(response.content)
