# Generated by Django 5.0.7 on 2024-09-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_order_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipment_status',
            field=models.BooleanField(default=False),
        ),
    ]
