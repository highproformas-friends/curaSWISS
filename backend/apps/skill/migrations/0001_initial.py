# Generated by Django 3.0.4 on 2020-03-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_needed', models.BooleanField(default=False)),
                ('short_text', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(default='')),
                ('bla', models.BooleanField(default=False)),
                ('valid_roles', models.ManyToManyField(to='role.Role')),
            ],
            options={
                'ordering': ['short_text'],
            },
        ),
    ]
