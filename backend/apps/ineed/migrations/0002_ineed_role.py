# Generated by Django 3.0.4 on 2020-03-28 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ineed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ineed',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ineed.Role'),
        ),
    ]
