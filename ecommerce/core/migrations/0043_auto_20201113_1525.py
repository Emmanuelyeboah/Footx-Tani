# Generated by Django 3.1 on 2020-11-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20201113_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='compratore',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
