# Generated by Django 3.1 on 2020-10-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazione', models.CharField(max_length=30)),
                ('regione', models.CharField(max_length=35)),
                ('provincia', models.CharField(max_length=30)),
                ('cap', models.CharField(max_length=5)),
                ('città', models.CharField(max_length=50)),
                ('via', models.CharField(max_length=50)),
                ('n_civico', models.CharField(max_length=10)),
                ('interno', models.CharField(blank=True, max_length=30)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]