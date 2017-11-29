# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0003_auto_20170801_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='endtime',
            field=models.TimeField(default=datetime.datetime(2017, 8, 1, 6, 12, 38, 60469, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
