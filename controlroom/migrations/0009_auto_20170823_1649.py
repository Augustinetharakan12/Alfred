# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0008_auto_20170810_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_list',
            field=models.CharField(default=0, max_length=200, blank=True),
        ),
    ]
