# Generated by Django 2.0.6 on 2018-07-19 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0017_auto_20180717_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='money_receive_date',
            field=models.DateField(default=datetime.datetime(2018, 7, 19, 15, 36, 13, 995899)),
            preserve_default=False,
        ),
    ]
