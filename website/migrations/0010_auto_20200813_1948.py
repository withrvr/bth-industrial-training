# Generated by Django 3.0.7 on 2020-08-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200813_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencemodels',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
