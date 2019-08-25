# Generated by Django 2.2.2 on 2019-07-30 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190730_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Dept2_rating',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='Dept3_rating',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='Dept4_rating',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
