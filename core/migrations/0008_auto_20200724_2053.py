# Generated by Django 3.0.8 on 2020-07-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200724_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='recipes', to='core.Tag'),
        ),
    ]
