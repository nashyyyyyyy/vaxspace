# Generated by Django 4.0 on 2023-12-06 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0018_schedule_vaccine_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='vax',
        ),
    ]
