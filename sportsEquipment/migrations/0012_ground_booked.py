# Generated by Django 2.1.5 on 2020-05-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsEquipment', '0011_addground'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='booked',
            field=models.TextField(default=';'),
        ),
    ]