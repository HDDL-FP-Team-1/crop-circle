# Generated by Django 3.0.8 on 2020-07-28 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200727_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='core.Farm'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='offsite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offsite_locations', to='core.OffSite'),
        ),
    ]
