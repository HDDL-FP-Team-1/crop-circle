# Generated by Django 3.0.8 on 2020-08-01 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_farm_about_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='hours',
        ),
        migrations.AddField(
            model_name='openhours',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='core.Farm'),
        ),
    ]
