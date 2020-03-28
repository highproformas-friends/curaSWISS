from django import forms
from .models import IOffer
from django.core.exceptions import ValidationError


from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,Field, Row, Column, Div, HTML
from apps.accounts.models import User

class IOfferForm(forms.ModelForm):
    class Meta:
        model = IOffer
        exclude = ['uuid', 'registration_date', 'user']
        #labels = form_labels
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
  HTML("<h2 class='form-heading'>{}</h2>".format(_("Persönliche Informationen"))),
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
                Column('plz', css_class='form-group col-md-4 mb-0'),
                Column('countrycode', css_class='form-group col-md-4 mb-0'),
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