# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0015_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_list',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
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
        migrations.AlterField(
            model_name='venue',
            name='vm_1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='venue',
            name='vm_2',
            field=models.CharField(default=b'nil', max_length=1000),
        ),
        migrations.AlterField(
            model_name='venue',
            name='vm_num_1',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='vm_num_2',
            field=models.CharField(default=b'nil', max_length=1000),
        ),
    ]
