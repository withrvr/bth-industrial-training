# Generated by Django 3.0.7 on 2020-08-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200813_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencemodels',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
