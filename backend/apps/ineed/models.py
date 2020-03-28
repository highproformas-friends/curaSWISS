from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):

    name = models.CharField(max_length=50, default='')


class INeed(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    organization_name = models.CharField(max_length=50, default='')

    plz = models.CharField(max_length=5, null=True)


    class Meta:
        ordering = ['plz']

