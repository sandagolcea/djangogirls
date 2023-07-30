from django.shortcuts import render
import requests

def geolocation(request):
    response = requests.get('http://www.geoplugin.net/json.gp')
    data = response.json()
    return render(request, 'geolocation.html', {
        'city': data['geoplugin_city'],
        'country': data['geoplugin_countryName']
    })
