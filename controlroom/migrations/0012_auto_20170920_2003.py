# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0011_auto_20170920_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_list',
            field=models.CharField(default=b'nil', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner1',
            field=models.CharField(default=True, max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner2',
            field=models.CharField(default=True, max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner3',
            field=models.CharField(default=True, max_length=60, blank=True),
        ),
    ]
