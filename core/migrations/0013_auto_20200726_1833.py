# Generated by Django 3.0.8 on 2020-07-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200726_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='farm',
        ),
        migrations.AddField(
            model_name='farm',
            name='crop',
            field=models.ManyToManyField(related_name='farm_crops', to='core.Crop'),
        ),
    ]
