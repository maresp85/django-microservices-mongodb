# Generated by Django 2.2.3 on 2019-08-02 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20190802_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='register',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 2, 17, 27, 36, 940339)),
        ),
    ]
