# Generated by Django 3.1 on 2020-10-19 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_payment_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='item',
        ),
    ]