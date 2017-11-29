# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0016_auto_20170927_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='power',
            field=models.CharField(default='kiran', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='power_num',
            field=models.CharField(default=b'nil', max_length=10),
        ),
        migrations.AlterField(
            model_name='venue',
            name='vm_num_1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='vm_num_2',
            field=models.CharField(default=b'nil', max_length=10),
        ),
    ]
