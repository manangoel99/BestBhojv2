# Generated by Django 2.0.6 on 2018-06-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0005_auto_20180623_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
