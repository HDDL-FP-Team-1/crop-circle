# Generated by Django 3.0.8 on 2020-08-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20200801_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openhours',
            options={},
        ),
        migrations.AddField(
            model_name='openhours',
            name='fri_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Friday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='fri_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Friday Opening Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='mon_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Monday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='mon_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Monday Opening Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='sat_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Saturday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='sat_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Saturday Opening Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='sun_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Sunday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='sun_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Sunday Opening Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='thu_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Thursday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='thu_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Thursday Opening Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='tue_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Tuesday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='tue_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Tuesday Opening Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='wed_end',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Wednesday Closing Time'),
        ),
        migrations.AddField(
            model_name='openhours',
            name='wed_start',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Wednesday Opening Time'),
        ),
        migrations.AlterUniqueTogether(
            name='openhours',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='openhours',
            name='from_hour',
        ),
        migrations.RemoveField(
            model_name='openhours',
            name='to_hour',
        ),
        migrations.RemoveField(
            model_name='openhours',
            name='weekday',
        ),
    ]
