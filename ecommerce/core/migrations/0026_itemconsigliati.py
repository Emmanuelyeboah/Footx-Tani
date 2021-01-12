# Generated by Django 3.1 on 2020-10-22 13:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0025_auto_20201022_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemConsigliati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoriaN', models.PositiveIntegerField()),
                ('categoriaA', models.PositiveIntegerField()),
                ('categoriaJ', models.PositiveIntegerField()),
                ('categoriaL', models.PositiveIntegerField()),
                ('categoriaO', models.PositiveIntegerField()),
                ('media_taglia', models.FloatField(validators=[django.core.validators.MinValueValidator(35.0), django.core.validators.MaxValueValidator(47.0)])),
                ('condizioneN', models.PositiveIntegerField()),
                ('condizioneU', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
