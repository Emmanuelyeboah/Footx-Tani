# Generated by Django 3.1 on 2020-10-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_payment_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingaddress',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
