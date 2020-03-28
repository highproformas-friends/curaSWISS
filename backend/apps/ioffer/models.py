from django.conf import settings
from django.db import models
from apps.accounts.models import User
from apps.role.models import Role, Function

# Create your models here.


class IOffer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    offer_functions = models.ManyToManyField(Function)

    name_first = models.CharField(max_length=50, default='')
    name_last = models.CharField(max_length=50, default='')

    plz = models.CharField(max_length=5, null=True)


    class Meta:
        ordering = ['plz']
