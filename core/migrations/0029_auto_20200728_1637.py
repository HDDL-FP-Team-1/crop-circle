# Generated by Django 3.0.8 on 2020-07-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_delete_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='location',
        ),
        migrations.AddField(
            model_name='farm',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
