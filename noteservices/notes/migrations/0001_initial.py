# Generated by Django 2.1.2 on 2019-08-01 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iduser', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=240)),
                ('register', models.DateField(default=datetime.datetime(2019, 8, 1, 11, 37, 40, 952947))),
            ],
        ),
    ]
