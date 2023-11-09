# Generated by Django 4.2.7 on 2023-11-09 21:49

import datetime
from django.db import migrations, models
import django.db.models.manager
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', django_jalali.db.models.jDateTimeField(blank=True, editable=False, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('mobile_phone', models.CharField(max_length=11, unique=True, verbose_name='شماره همراه')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='خانوادگی')),
                ('birth_day', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', django_jalali.db.models.jDateTimeField(blank=True, default=datetime.datetime(2023, 11, 9, 21, 49, 41, 550869, tzinfo=datetime.timezone.utc), null=True, verbose_name='date joined')),
                ('update_information', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='update user')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='RecycleUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('deleted', django.db.models.manager.Manager()),
            ],
        ),
    ]
