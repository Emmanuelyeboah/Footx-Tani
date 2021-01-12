# Generated by Django 3.1 on 2020-10-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201009_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.orderitem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.item'),
        ),
    ]
