# Generated by Django 3.0.4 on 2020-03-29 17:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ineed', '0003_ineed_needed_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ineed',
            name='email',
        ),
        migrations.AlterField(
            model_name='ineed',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, unique=True),
        ),
    ]
