# Generated by Django 3.0.8 on 2020-08-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_merge_20200803_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='street_address_line_2',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Street Address Line 2'),
        ),
    ]
