# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_userinfo_participated_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='paid_userinfo',
            fields=[
                ('excelid', models.CharField(default=b'excel', max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('college', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=50, unique=True, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('present', models.BooleanField(default=False)),
                ('stay', models.BooleanField(default=False)),
                ('event', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'paid_userinfo',
                'verbose_name_plural': 'paid_userinfos',
            },
        ),
        migrations.CreateModel(
            name='paid_winners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excelid', models.CharField(max_length=30, blank=True)),
                ('event', models.CharField(max_length=50, blank=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('college', models.CharField(max_length=50, blank=True)),
                ('position', models.IntegerField(default=0)),
                ('printed', models.BooleanField(default=False)),
            ],
        ),
    ]
