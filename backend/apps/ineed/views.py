from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import INeedForm
from django.http import HttpResponse, HttpResponseRedirect

def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = INeedForm(request.POST or None)

        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks')
        else:
            print(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = INeedForm()

    context = { 'form': form }

    return render(request, 'ineed_signup.html', context)