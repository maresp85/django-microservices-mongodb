# Generated by Django 2.2.3 on 2019-08-02 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercrud', '0005_auto_20190802_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_register',
            field=models.DateField(default=datetime.datetime(2019, 8, 2, 17, 27, 15, 604457)),
        ),
    ]
