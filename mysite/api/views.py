import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

url="https://api.coingecko.com/api"
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def GekoAPI_getStatus(request):
    response= requests.get(url + "/v3/ping")

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_simple_priece(request):
    response= requests.get(url+'/v3/simple/price', params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_coinList(request):
    response= requests.get(url + "/v3/coins/list", params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_assetPlatforms(request):
    response= requests.get(url + "/v3/asset_platforms", params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_coinsCategories(request):
    response= requests.get(url + "/v3/coins/categories")

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_exchangesList(request):
    response= requests.get(url + "/v3/exchanges", params=request.GET) #revisar pq no cambia

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_indexes(request):
    response= requests.get(url + "/v3/indexes", params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_derivatives(request):
    response= requests.get(url + "/v3/derivatives", params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_nftsList(request):
    response= requests.get(url + "/v3/nfts/list", params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_exchangeRates(request):
    response= requests.get( url + "/v3/exchange_rates")

    return HttpResponse(response.content, status= response.status_code)
#print(request.GET)
def GekoAPI_search(request):
    response= requests.get(url + "/v3/search", params=request.GET)

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_searchTrending(request):
    response= requests.get(url + "/v3/search/trending")

    return HttpResponse(response.content, status= response.status_code)

def GekoAPI_global(request):
    response= requests.get(url + "/v3/global")

    return HttpResponse(response.content, status= response.status_code)


def GekoAPI_coins_markets(request):
    response= requests.get(url+'/v3/coins/markets', params=request.GET)

    return HttpResponse(response.content, status= response.status_code)










