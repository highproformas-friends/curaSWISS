from django.shortcuts import render
from apps.ioffer.models import IOffer
from apps.location.models import ZipCode

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoibnNpaWNtMCIsImEiOiJjazhjNDJkd2cwaW5iM2twaTM4ZXZrcm10In0.efXuicWK6cjTrJJjWp1jQA'
    functions, offers = fetch_functions()
    coordinates = map_postalcodes_with_coordinates(offers)
    return render(request, 'map.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'functions':functions,
                   'offers': offers,
                   'coordinates': coordinates})

def fetch_functions():
    ioffers = IOffer.objects.all() #here we could do some filtering
    offered_functions = dict()
    functions = list()
    for ioffer in ioffers:
        plz = ioffer.location.plz
        funcs = [f.short_text for f in ioffer.offer_functions.all()]
        functions.extend(funcs)
        func_counts = dict()

        for f in set(funcs):
            func_counts[f] = funcs.count(f)

        if plz not in offered_functions:
            offered_functions[plz] = func_counts
        else:
            offered_functions[plz] = (offered_functions[plz]).update(func_counts)

    return list(set(functions)), offered_functions

def map_postalcodes_with_coordinates(offers):
    plzs = offers.keys()
    zipcodes = ZipCode.objects.filter(plz__in=plzs)
    postalcodes_map = dict()
    for location in zipcodes: # here we will run into problems since certain places have the same zipcode.
        postalcodes_map[location.plz] = {'lat':str(location.lat), 'lng': str(location.lng), 'locality': location.locality}
    return postalcodes_map
