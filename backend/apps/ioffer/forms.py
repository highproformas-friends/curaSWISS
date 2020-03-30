from django import forms
from .models import IOffer
from django.core.exceptions import ValidationError
from django_select2.forms import Select2Widget, ModelSelect2Widget

from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,Field, Row, Column, Div, HTML
from apps.accounts.models import User
from apps.location.models import CountryCode, ZipCode

form_labels = {
    'uuid': _('Writer'),
    'registration_date': _('Writer'),

    'name_first': _('Vorname'),
    'name_last': _('Nachname'),
    'phone_number': _('Telefonnummer'),

    'plz': _('Postleitzahl'),
    'countrycode': _('Land'),
    'email': _('Email'),
    'availability_start': _('Ich bin verfügbar ab'),

    'braucht_bezahlung': _('Ich benötige eine Vergütung'),
    'sonstige_qualifikationen': _('Weitere Qualifikationen'),
    'datenschutz_zugestimmt': _('Hiermit akzeptiere ich die <a href="/dataprotection/">Datenschutzbedingungen</a>.'),
    'einwilligung_datenweitergabe': _(
        'Ich bestätige, dass meine Angaben korrekt sind und ich der Institution meinen Ausbildungsstand nachweisen kann. Mit der Weitergabe meiner Kontaktdaten an die Institutionen bin ich einverstanden.'),
'zeitliche_verfuegbarkeit': _('Zeitliche Verfügbarkeit, bis zu'),
    'role': _('Rolle'),
    'location': _('Ortschaft'),
}


class IOfferForm(forms.ModelForm):
    class Meta:
        model = IOffer
        exclude = ['uuid', 'registration_date', 'user']
        labels = form_labels
        help_texts = {
            'email': _('Über diese Emailadresse dürfen dich medizinische Einrichtungen kontaktieren'),
            'countrycode': _('Bitte wähle ein Land aus'),
            'plz': _('bevorzugter Einsatzort (bei mehreren bitte mehrere Accounts erstellen)')
        }

    def __init__(self, *args, **kwargs):
        super(IOfferForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False

        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.layout = Layout(
  HTML("<h2 class='form-heading'>{}</h2>".format(_("Wo willst du helfen?"))),
            Row(
                Column('role', css_class='form-group col-md-6 mb-0'),
                # Column('offer_functions', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                HTML("<div id='ajax_functions_placeholder' class='form-group col-md-12 mb-0'></div>"),
                css_class='form-row'
            ),
  HTML("<hr style='margin-top: 30px; margin-bottom:30px;'><h2 class='form-heading'>{}</h2>".format(_("Persönliche Informationen"))),
            Row(
                Column('name_first', css_class='form-group col-md-6 mb-0'),
                Column('name_last', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone_number', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            HTML("<hr style='margin-top: 30px; margin-bottom:30px;'><h2 class='form-heading'>{}</h2>".format(_("Über deinen Einsatz"))),
            Row(
                Column('countrycode', css_class='form-group col-md-4 mb-0'),
                Column('location', css_class='form-group col-md-4 mb-0'),
                Column('umkreis', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('availability_start', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('braucht_bezahlung', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ), Row(
                Column('zeitliche_verfuegbarkeit', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),Row(
                Column('unterkunft_gewuenscht', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ))

        self.helper.layout.extend((
            'sonstige_qualifikationen'
            ,
            HTML('<hr style="margin-top: 20px; margin-bottom:30px;">'),
            HTML('<p class="text-left">'),
            'datenschutz_zugestimmt',
            HTML("</p>"),
            HTML('<p class="text-left">'),
            'einwilligung_datenweitergabe',
            HTML("</p>"),
            HTML('<div class="registration_disclaimer">{}</div>'.format(_('Die Bereitstellung unseres Services erfolgt unentgeltlich. Mir ist bewusst, dass die Ausgestaltung des Verhältnisses zur Institution allein mich und die entsprechende Institution betrifft. Insbesondere Art und Umfang der Arbeit, eine etwaige Vergütung und vergleichbares betreffen nur mich und die entsprechende Institution. Eine Haftung von curaSWISS ist ausgeschlossen.'))),
            Submit('submit', _('Registriere mich'), css_class='btn blue text-white btn-md',
                   onclick="this.form.submit(); this.disabled=true; this.value='Sending…';"),
        ))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Diese Email ist bereits vergeben"))
        return email


class IOfferFormAndMail(IOfferForm):
    email = forms.EmailField()
    countrycode = forms.ModelChoiceField(queryset=CountryCode.objects.all().order_by('code_alpha_2'),
                                         widget=Select2Widget, label=_("Land"))

    location = forms.ModelChoiceField(
        queryset=ZipCode.objects.all(),
        label=_("Ortschaft"),
        widget=ModelSelect2Widget(
            model=ZipCode,
            search_fields=['plz__icontains', 'locality__icontains'],
            dependent_fields={'countrycode': 'country_code'},
            max_results=500,
        )
    )