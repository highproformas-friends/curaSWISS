from django.db import transaction
from django.shortcuts import render

# Create your views here.
from apps.accounts.models import User
from django.http import HttpResponse
from django.template import loader
from apps.accounts.utils import send_password_set_email
from .forms import INeedForm, INeedFormAndMail
from apps.ineed.models import INeed
from django.http import HttpResponse, HttpResponseRedirect

def thanks(request):
    return render(request, 'ineed_thanks.html', {})

def sign_up(request):
    
    if request.method == 'POST':
        form = INeedFormAndMail(request.POST or None)
        
        if form.is_valid():
            register_ineed_in_db(request, mail=form.cleaned_data['email'])
            send_password_set_email(
                email=form.cleaned_data['email'],
                host=request.META['HTTP_HOST'],
                subject_template="registration/password_reset_email_subject.txt"
            )
            return HttpResponseRedirect('/ineed/thanks')
        else:
            print(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = INeedFormAndMail()

    context = { 'form': form }

    return render(request, 'ineed_signup.html', context)


@transaction.atomic
def register_ineed_in_db(request, mail):
    pwd = User.objects.make_random_password()
    username = mail
    user = User.objects.create(username=username, email=username)
    user.set_password(pwd)
    user.save()

    ineed = INeed.objects.create(user=user)
    ineed = INeedForm(request.POST, instance=ineed)
    ineed.save()

    return user, ineed