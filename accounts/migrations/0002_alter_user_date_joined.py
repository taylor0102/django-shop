# Generated by Django 4.2.7 on 2023-11-09 21:58

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 11, 9, 21, 58, 0, 927493, tzinfo=datetime.timezone.utc), null=True, verbose_name='date joined'),
        ),
    ]