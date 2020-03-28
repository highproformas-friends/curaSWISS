from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def test(request):
    return HttpResponse('Hello, welcome to the index page.')


def test_template(request):
    template = loader.get_template('test.html')
    context = {
        'test': 'abc'
    }
    return HttpResponse(template.render(context, request))

