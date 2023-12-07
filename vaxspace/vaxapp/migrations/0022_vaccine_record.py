# Generated by Django 4.0 on 2023-12-07 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vaxapp', '0021_remove_register_vaccine_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_info', models.JSONField(default=None)),
                ('child', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]