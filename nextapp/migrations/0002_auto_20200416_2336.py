# Generated by Django 2.1 on 2020-04-16 23:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relaygroup',
            name='r_lastupdateinfo',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 23, 36, 40, 175183)),
        ),
    ]
