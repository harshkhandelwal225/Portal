# Generated by Django 2.2.2 on 2019-07-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190718_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='Average_Rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
