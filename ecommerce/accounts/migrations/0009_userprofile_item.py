# Generated by Django 3.1 on 2020-10-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order_orderitem'),
        ('accounts', '0008_auto_20201008_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='item',
            field=models.ManyToManyField(blank=True, to='core.Item'),
        ),
    ]
