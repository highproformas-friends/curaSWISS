# Generated by Django 3.0.4 on 2020-03-29 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('ineed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ineed',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location.ZipCode'),
        ),
    ]
