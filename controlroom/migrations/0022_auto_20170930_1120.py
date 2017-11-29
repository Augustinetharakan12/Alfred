# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0021_auto_20170930_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='em_num',
            field=models.CharField(default=1234567890, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.CharField(default=b'nil', max_length=10000, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_list',
            field=models.CharField(default=b'nil', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner1',
            field=models.CharField(default=b'nil', max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner2',
            field=models.CharField(default=b'nil', max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner3',
            field=models.CharField(default=b'nil', max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='current_event',
            field=models.CharField(default=b'nil', max_length=15),
        ),
        migrations.AlterField(
            model_name='venue',
            name='next_event',
            field=models.CharField(default=b'nil', max_length=15),
        ),
    ]
