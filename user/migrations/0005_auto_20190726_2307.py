# Generated by Django 2.2.2 on 2019-07-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190723_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='Dept1_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Dept2_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Dept3_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='Dept4_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
