# Generated by Django 3.0.8 on 2020-07-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200722_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='item',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
