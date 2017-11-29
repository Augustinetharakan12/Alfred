# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0022_auto_20170930_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='power_num',
            field=models.CharField(max_length=10),
        ),
    ]
