# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0019_auto_20170929_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='current_event',
            field=models.CharField(default=b'Nil', max_length=15),
        ),
        migrations.AlterField(
            model_name='venue',
            name='next_event',
            field=models.CharField(max_length=15),
        ),
    ]
