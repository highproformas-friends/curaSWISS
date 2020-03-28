from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def sign_up(request):
    return render(request, 'ineed_signup.html', {})


