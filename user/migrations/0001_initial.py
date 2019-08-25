# Generated by Django 2.2.2 on 2019-07-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=30)),
                ('Item_desc', models.CharField(max_length=30)),
                ('Vendor_name', models.CharField(max_length=30)),
                ('Vendor_loc', models.CharField(max_length=30)),
                ('Approval', models.CharField(max_length=30)),
                ('Average_Rating', models.IntegerField()),
                ('Project', models.IntegerField()),
                ('Project_Rating', models.IntegerField()),
                ('Comm_dept1', models.CharField(max_length=100)),
                ('Comm_dept2', models.CharField(max_length=100)),
                ('Comm_dept3', models.CharField(max_length=100)),
                ('Comm_dept4', models.CharField(max_length=100)),
            ],
        ),
    ]
