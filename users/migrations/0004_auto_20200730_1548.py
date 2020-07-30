# Generated by Django 3.0.8 on 2020-07-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20200729_1928'),
        ('users', '0003_auto_20200728_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farms', to='core.Farm'),
        ),
    ]
