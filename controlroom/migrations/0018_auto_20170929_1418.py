# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0017_auto_20170927_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.CharField(max_length=15, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue_id',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_id',
            field=models.CharField(max_length=3, serialize=False, primary_key=True),
        ),
    ]
