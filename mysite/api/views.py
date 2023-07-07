import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

url="https://api.coingecko.com/api"
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def GekoAPI_getStatus(request):
    response= requests.get('https://api.coingecko.com/api/v3/ping')

    return HttpResponse(response.content)

def GekoAPI_coinList(request):
    response= requests.get('https://api.coingecko.com/api/v3/coins/list')

    return HttpResponse(response.content)

def GekoAPI_assetPlatforms(request):
    response= requests.get('https://api.coingecko.com/api/v3/asset_platforms')

    return HttpResponse(response.content)

def GekoAPI_coinsCategories(request):
    response= requests.get('https://api.coingecko.com/api/v3/coins/categories')

    return HttpResponse(response.content)

def GekoAPI_exchangesList(request):
    response= requests.get('https://api.coingecko.com/api/v3/exchanges/list')

    return HttpResponse(response.content)

def GekoAPI_indexes(request):
    response= requests.get('https://api.coingecko.com/api/v3/indexes')

    return HttpResponse(response.content)

def GekoAPI_derivatives(request):
    response= requests.get('https://api.coingecko.com/api/v3/derivatives')

    return HttpResponse(response.content)

def GekoAPI_nftsList(request):
    response= requests.get('https://api.coingecko.com/api/v3/nfts/list')

    return HttpResponse(response.content)

def GekoAPI_exchangeRates(request):
    response= requests.get('https://api.coingecko.com/api/v3/exchange_rates')

    return HttpResponse(response.content)

def GekoAPI_search(request):
    print(request.GET)
    response= requests.get('https://api.coingecko.com/api/v3/search',params=request.GET)

    return HttpResponse(response.content)

def GekoAPI_searchTrending(request):
    response= requests.get('https://api.coingecko.com/api/v3/search/trending')

    return HttpResponse(response.content)

def GekoAPI_global(request):
    response= requests.get('https://api.coingecko.com/api/v3/global')

    return HttpResponse(response.content)

def GekoAPI_simple_priece(request):
    response= requests.get(url+'/v3/simple/price',params=request.GET)

    return HttpResponse(response.content,status= response.status_code)

def GekoAPI_coins_markets(request):
    response= requests.get(url+'/v3/coins/markets',params=request.GET)

    return HttpResponse(response.content,status= response.status_code)










