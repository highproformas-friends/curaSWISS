# Generated by Django 3.0.4 on 2020-03-29 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ineed', '0004_auto_20200329_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ineed',
            options={},
        ),
        migrations.RemoveField(
            model_name='ineed',
            name='zip_code',
        ),
    ]
