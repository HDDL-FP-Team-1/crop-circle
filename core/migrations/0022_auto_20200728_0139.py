# Generated by Django 3.0.8 on 2020-07-28 01:39

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200728_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=mapbox_location_field.models.AddressAutoHiddenField(map_id='map', null=True),
        ),
    ]
