# Generated by Django 3.0.7 on 2020-08-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200813_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencemodels',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
