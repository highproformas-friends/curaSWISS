from django.shortcuts import render
from apps.ioffer.models import IOffer
def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoibnNpaWNtMCIsImEiOiJjazhjNDJkd2cwaW5iM2twaTM4ZXZrcm10In0.efXuicWK6cjTrJJjWp1jQA'
    functions, offers = fetch_functions()
    return render(request, 'map.html',
                  {'mapbox_access_token': mapbox_access_token,
                   'functions':functions, 'offers': offers})

def fetch_functions():
    ioffers = IOffer.objects.all() #here we could do some filtering
    offered_functions = dict()
    functions = list()
    for ioffer in ioffers:
        plz = ioffer.plz
        role = ioffer.role
        funcs = [f.name for f in role.functions.all()]
        functions.extend(funcs)
        func_counts = dict()
        for f in set(funcs):
            func_counts[f] = funcs.count(f)
        if plz not in offered_functions:
            offered_functions[plz] = func_counts
        else:
            offered_functions[plz] = (offered_functions[plz]).update(func_counts)
    return list(set(functions)), offered_functions