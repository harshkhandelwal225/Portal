# Generated by Django 2.2.2 on 2019-08-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20190806_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Approval',
            field=models.CharField(max_length=30),
        ),
    ]
