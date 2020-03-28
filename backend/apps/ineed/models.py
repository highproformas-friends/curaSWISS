from django.conf import settings
from django.db import models
from apps.accounts.models import User

# Create your models here.
class Role(models.Model):

    ROLES = [
        "ROLE1",
        "ROLE2"
    ]

    name = models.CharField(max_length=50, default=ROLES)


class INeed(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=Role.ROLES[0])

    organization_name = models.CharField(max_length=50, default='')

    plz = models.CharField(max_length=5, null=True)


    class Meta:
        ordering = ['plz']

