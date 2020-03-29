from django.db import models

# Create your models here.


class CountryCode(models.Model):

    code_alpha_2 = models.CharField(max_length=2, unique=True)


    def __str__(self):
        return self.code_alpha_2

class ZipCode(models.Model):

    country_code = models.ForeignKey(CountryCode, on_delete=models.CASCADE)

    plz = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    locality = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.locality

