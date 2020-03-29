from django.forms import *
from django.db import models
from django import forms
from django_select2.forms import Select2Widget, ModelSelect2Widget

from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Row, Column, Div
from apps.ineed.models import INeed
from apps.location.models import CountryCode, ZipCode

class INeedForm(ModelForm):

    class Meta:
        model = INeed
        exclude = ['uuid', 'registration_date', 'user', 'is_approved','role']

        help_texts = {
            'sonstige_infos': _('Einsatzbereiche? Anforderungen? ... und nette Worte :)')
        }

        labels = {
            'zip_code': _('Postleitzahl'),
            'role': _('Rolle'),
            'countrycode': _('Land'),
            'organization_name': _('Name der Institution'),
            'phone_number': _('Telefonnummer'),
            'appears_in_map': _('Sichtbar und kontaktierbar für Helfende sein'),
            'other_information': _('Wichtige Infos über Sie und den potentiellen Einsatzbereich'),
            'responsible_person': _('Ansprechpartner')
        }

    def __init__(self, *args, **kwargs):
        super(INeedForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.layout = Layout(
                Row(Column('organization_name') , Column('responsible_person')),
                Row(Column('appears_in_map')),
                Row(Column('phone_number'), Column('email')),
                Row(Column('countrycode'), Column('location')),
                Row(Column('other_information'))
        )

        self.helper.layout.extend((
            HTML('<hr style="margin-top: 20px; margin-bottom:30px;">'),
            HTML('<p class="text-left">'),
            'datenschutz_zugestimmt',
            HTML("</p>"),
            HTML('<p class="text-left">'),
            'einwilligung_datenweitergabe',
            HTML("</p>"),
            HTML('<div class="registration_disclaimer">{}</div>'.format(_('Die Bereitstellung unseres Services erfolgt unentgeltlich. Mir ist bewusst, dass die Ausgestaltung des Verhältnisses zur Institution allein mich und die entsprechende Institution betrifft. Insbesondere Art und Umfang der Arbeit, eine etwaige Vergütung und vergleichbares betreffen nur mich und die entsprechende Institution. Eine Haftung von curaSWISS ist ausgeschlossen.'))),
            Submit('submit', _('Jetzt registrieren'), css_class='btn blue text-white btn-md',
                   onclick="this.form.submit(); this.disabled=true; this.value='Sending…';"),
        ))


class INeedFormAndMail(INeedForm):
    email = forms.EmailField()
    countrycode = forms.ModelChoiceField(queryset=CountryCode.objects.all().order_by('code_alpha_2'),
                                         widget=Select2Widget)

    location = forms.ModelChoiceField(
        queryset=ZipCode.objects.all(),
        label=u"Location",
        widget=ModelSelect2Widget(
            model=ZipCode,
            search_fields=['plz__icontains', 'locality__icontains'],
            dependent_fields={'countrycode': 'country_code'},
            max_results=500,
        )
    )