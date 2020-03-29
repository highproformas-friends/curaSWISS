from django.conf import settings
from django.db import models

# Create your models here.


class Function(models.Model):

    name = models.CharField(max_length=50, unique=True)
    short_text = models.CharField(max_length=20, default='')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.short_text


class Role(models.Model):

    NAME_CHOICES = [
        ("MEDICAL", 'Medicine'),
        ("SHOPPING", 'Shopping'),
    ]
    name = models.CharField(max_length=50, choices=NAME_CHOICES, default='MEDICAL')

    functions = models.ManyToManyField(Function, related_name='functions')
    short_text = models.CharField(max_length=20, default='', unique=True)

    ## There should be a validation that funtions and name are not combined the same way
    ## several times. Check Meta keyword unique_together later... Functions are n:m to roles
    ## could be difficult to validate.

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.short_text

