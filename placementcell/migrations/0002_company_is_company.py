# Generated by Django 5.0.2 on 2024-02-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placementcell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_company',
            field=models.BooleanField(default=False),
        ),
    ]
