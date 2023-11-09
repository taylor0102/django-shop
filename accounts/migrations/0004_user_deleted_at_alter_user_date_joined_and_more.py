# Generated by Django 4.2.7 on 2023-11-08 19:54

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=django_jalali.db.models.jDateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 11, 8, 19, 54, 48, 923496, tzinfo=datetime.timezone.utc), null=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, editable=False, null=True),
        ),
    ]