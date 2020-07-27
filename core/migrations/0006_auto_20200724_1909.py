# Generated by Django 3.0.8 on 2020-07-24 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_crop_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmers', to=settings.AUTH_USER_MODEL),
        ),
    ]
