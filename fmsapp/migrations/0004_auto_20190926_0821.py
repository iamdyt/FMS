# Generated by Django 2.2.2 on 2019-09-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsapp', '0003_auto_20190926_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='country',
            field=models.CharField(default='Nigeria', max_length=20),
        ),
        migrations.AddField(
            model_name='staff',
            name='state',
            field=models.CharField(choices=[('edo', 'Edo'), ('ekiti', 'Ekiti'), ('kogi', 'Kogi'), ('kwara', 'Kwara'), ('lagos', 'Lagos'), ('ogun', 'Ogun'), ('ondo', 'Ondo'), ('osun', 'Osun'), ('oyo', 'Oyo')], default='edo', max_length=20),
        ),
    ]
