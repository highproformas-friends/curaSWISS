from django.conf import settings
from django.db import models
from apps.accounts.models import User
import uuid
from datetime import datetime
from apps.role.models import Role, Function
from apps.location.models import ZipCode

# Create your models here.


class INeed(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    needed_functions = models.ManyToManyField(Function)

    location = models.ForeignKey(ZipCode, on_delete=models.CASCADE, null=True)

    organization_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=100,default='')
    zip_code = models.CharField(max_length=5, null=True)
    other_information = models.TextField(default='')
    responsible_person = models.CharField(max_length=100,default='')
    email = models.EmailField(unique=True)

    uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    registration_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    appears_in_map = models.BooleanField(default=True)
    
    # Hard coded... :-( Multiple values for later use
    COUNTRY_CODE_CHOICES = [
        # ("DE", 'Deutschland'),
        # ("AT", 'Österreich'),
        ("CH", 'Schweiz'),
    ]
    countrycode = models.CharField(
        max_length=2,
        choices=COUNTRY_CODE_CHOICES,
        default="CH",
    )

    class Meta:
        ordering = ['zip_code']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.uuid

    # def clean(self):
    #     if self.plz not in plzs[self.countrycode]:
    #         raise ValidationError(_(str(self.plz) + " ist keine Postleitzahl in " + self.countrycode))


