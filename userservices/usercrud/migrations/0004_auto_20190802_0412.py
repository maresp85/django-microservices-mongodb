# Generated by Django 2.2.3 on 2019-08-02 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercrud', '0003_auto_20190801_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_register',
            field=models.DateField(default=datetime.datetime(2019, 8, 2, 4, 12, 5, 234380)),
        ),
    ]
