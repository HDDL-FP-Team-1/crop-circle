# Generated by Django 3.0.8 on 2020-07-29 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20200729_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crops', to='core.Farm'),
        ),
    ]