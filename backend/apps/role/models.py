from django.conf import settings
from django.db import models

# Create your models here.


class Function(models.Model):

    name = models.CharField(max_length=50)


class Role(models.Model):

    functions = models.ManyToManyField(Function, related_name='functions')

    NAME_CHOICES = [
        ("MEDICAL", 'Medicine Role'),
        ("NEXT", 'Next Role'),
    ]

    name = models.CharField(max_length=50, choices=NAME_CHOICES, default='MEDICAL')

    class Meta:
        ordering = ['name']



