# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0004_event_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='winner1',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner2',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='winner3',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
