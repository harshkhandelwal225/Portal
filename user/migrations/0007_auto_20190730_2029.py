# Generated by Django 2.2.2 on 2019-07-30 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190730_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Comm_dept1',
            field=models.CharField(blank=True, max_length=500, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
