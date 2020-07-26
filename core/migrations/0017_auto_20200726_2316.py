# Generated by Django 3.0.8 on 2020-07-26 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_offsite_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='crop',
        ),
        migrations.RemoveField(
            model_name='offsite',
            name='crop',
        ),
        migrations.AddField(
            model_name='crop',
            name='farm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crops', to='core.Farm'),
        ),
        migrations.AddField(
            model_name='crop',
            name='offsite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offsite_crops', to='core.OffSite'),
        ),
    ]
