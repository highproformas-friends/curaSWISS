from django.conf import settings
from django.db import models
from apps.accounts.models import User

# Create your models here.
class Role(models.Model):

    name = models.CharField(max_length=50)


class INeed(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    organization_name = models.CharField(max_length=50, default='')

    plz = models.CharField(max_length=5, null=True)


    class Meta:
        ordering = ['plz']

