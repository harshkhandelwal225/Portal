# Generated by Django 2.2.2 on 2019-08-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20190731_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Approval',
            field=models.CharField(default='Approved', max_length=30),
        ),
    ]
