# Generated by Django 2.2.2 on 2019-08-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20190806_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Approval',
            field=models.CharField(default='Approved', max_length=30),
        ),
    ]
