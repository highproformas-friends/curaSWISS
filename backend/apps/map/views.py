from django.shortcuts import render

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoibnNpaWNtMCIsImEiOiJjazhjNDJkd2cwaW5iM2twaTM4ZXZrcm10In0.efXuicWK6cjTrJJjWp1jQA'
    return render(request, 'map.html',
                  {'mapbox_access_token': mapbox_access_token})