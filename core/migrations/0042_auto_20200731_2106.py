# Generated by Django 3.0.8 on 2020-07-31 21:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0041_auto_20200731_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_farms', to=settings.AUTH_USER_MODEL),
        ),
    ]
