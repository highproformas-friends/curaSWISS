from django.contrib import admin
from .models import CountryCode, ZipCode
# Register your models here.

admin.site.register(CountryCode)
admin.site.register(ZipCode)
