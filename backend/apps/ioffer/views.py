from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from apps.ioffer.forms import IOfferForm


def sign_up(request):
    if request.method == 'POST':
        form = IOfferForm(request.POST)

        # # check whether it's valid:
        # if form.is_valid():
        #     user, student = register_student_in_db(request, mail=form.cleaned_data['email'])
        #     send_password_set_email(
        #         email=form.cleaned_data['email'],
        #         host=request.META['HTTP_HOST'],
        #         subject_template="registration/password_reset_email_subject.txt"
        #     )
        #     return HttpResponseRedirect("/iamstudent/thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IOfferForm()

    return render(request, 'ioffer_signup.html', {'form': form})


