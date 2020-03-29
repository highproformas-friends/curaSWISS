import uuid as uuid
from django.utils import timezone


from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from apps.accounts.models import User
from apps.role.models import Role, Function
from apps.location.models import ZipCode

# Create your models here.
LESSTEN = 1
LESSTWENTY = 2
LESSFOURTY = 3
MOREFOURTY = 4

UMKREIS_CHOICES = (
    (LESSTEN, '<10 km'),
    (LESSTWENTY, '<20 km'),
    (LESSFOURTY, '<40 km'),
    (MOREFOURTY, '>40 km'),
)

BEZAHLUNG = 1
UNENTGELTLICH = 2
BEZAHLUNG_CHOICES = (
    (UNENTGELTLICH, ('Ich freue mich über eine Vergütung, helfe aber auch ohne')),
    (BEZAHLUNG, ('Ich benötige eine Vergütung')),
)

TEN = 1
TWENTY = 2
THIRTY = 3
FOURTY = 4
VERFUEGBARKEIT_CHOICES = (
    (TEN, ('10h pro Woche')),
    (TWENTY, ('20h pro Woche')),
    (THIRTY, ('30h pro Woche')),
    (FOURTY, ('40h pro Woche')),
)


def validate_checkbox(value):
    if not value:
        raise ValidationError(_("Zustimmung erforderlich."), code='invalid')
    else:
        return value


class IOffer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    offer_functions = models.ManyToManyField(Function)

    location = models.ForeignKey(ZipCode, on_delete=models.CASCADE, null=True)

    name_first = models.CharField(max_length=50, default='')
    name_last = models.CharField(max_length=50, default='')

    uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    registration_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    phone_number = models.CharField(max_length=100, blank=True, default='')

    umkreis = models.IntegerField(choices=UMKREIS_CHOICES, null=True, blank=False)
    availability_start = models.DateField(null=True,default=timezone.now)

    braucht_bezahlung = models.IntegerField(choices=BEZAHLUNG_CHOICES,
                                            default=UNENTGELTLICH)

    zeitliche_verfuegbarkeit = models.IntegerField(choices=VERFUEGBARKEIT_CHOICES, null=True, blank=False)

    datenschutz_zugestimmt = models.BooleanField(default=False, validators=[validate_checkbox])
    einwilligung_datenweitergabe = models.BooleanField(default=False, validators=[validate_checkbox])

    sonstige_qualifikationen = models.CharField(max_length=200, blank=True, default='keine')
    unterkunft_gewuenscht = models.BooleanField(default=False)

    # Metadata
    class Meta:
        ordering = ['plz']

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user.email
