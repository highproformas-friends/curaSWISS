from django.db import models

# Create your models here.


class CountryCode(models.Model):

    code_alpha_2 = models.CharField(max_length=2, unique=True)


class ZipCode(models.Model):

    country_code = models.ForeignKey(CountryCode, on_delete=models.CASCADE)

    zip = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    locality = models.CharField(max_length=50, null=False)

