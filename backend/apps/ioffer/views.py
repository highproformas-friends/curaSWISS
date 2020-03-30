from django.db import transaction
from django.shortcuts import render

from django.http import HttpResponseRedirect

from apps.accounts.models import User
from apps.accounts.utils import send_password_set_email
from apps.ioffer.forms import IOfferForm, IOfferFormAndMail
from apps.ioffer.models import IOffer
from apps.role.models import Function, Role


def thanks(request):
    return render(request, 'ioffer_thanks.html', {})


def load_functions(request):
    role_id = request.GET.get('role')
    role = Role.objects.filter(id=role_id).first()
    functions = role.functions.all()

    return render(request, 'ioffer_functions_partial.html', {'functions': functions})


def sign_up(request):
    if request.method == 'POST':
        form = IOfferFormAndMail(request.POST)

        if form.is_valid():
            register_ioffer_in_db(request, mail=form.cleaned_data['email'])
            send_password_set_email(
                email=form.cleaned_data['email'],
                host=request.META['HTTP_HOST'],
                subject_template="registration/password_reset_email_subject.txt"
            )
            return HttpResponseRedirect("/ioffer/thanks")
    else:
        form = IOfferFormAndMail()

    return render(request, 'ioffer_signup.html', {'form': form})


@transaction.atomic
def register_ioffer_in_db(request, mail):
    pwd = User.objects.make_random_password()
    username = mail
    user = User.objects.create(username=username, email=username)
    user.set_password(pwd)
    user.save()

    ioffer = IOffer.objects.create(user=user)
    ioffer = IOfferForm(request.POST, instance=ioffer)
    ioffer.save()

    return user, ioffer


