# Generated by Django 4.0 on 2023-12-01 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0006_remove_schedule_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='brgy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaxapp.barangay'),
        ),
    ]
