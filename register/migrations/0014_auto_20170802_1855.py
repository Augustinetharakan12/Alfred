# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20170622_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='winners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excelid', models.CharField(max_length=30, blank=True)),
                ('event', models.CharField(max_length=50, blank=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('college', models.CharField(max_length=50, blank=True)),
                ('position', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='stay',
            field=models.BooleanField(default=False),
        ),
    ]
