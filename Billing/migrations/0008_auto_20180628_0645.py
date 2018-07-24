# Generated by Django 2.0.6 on 2018-06-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0007_orders_delivery_boy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order',
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity_100',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity_125',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity_150',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity_200',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity_60',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity_75',
            field=models.IntegerField(default=0),
        ),
    ]
