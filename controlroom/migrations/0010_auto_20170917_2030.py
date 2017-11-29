# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0009_auto_20170823_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_list',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
