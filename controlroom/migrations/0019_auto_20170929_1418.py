# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0018_auto_20170929_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue_id',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_id',
            field=models.CharField(max_length=4, serialize=False, primary_key=True),
        ),
    ]
