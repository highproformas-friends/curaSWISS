# Generated by Django 3.0.4 on 2020-03-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0003_remove_skill_bla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='short_text',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
