# Generated by Django 5.0.7 on 2024-09-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_transactiondetail_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiondetail',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
