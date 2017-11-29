# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0002_event_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='venue_id',
            field=models.CharField(max_length=3, serialize=False, primary_key=True, choices=[(b'201', b'201'), (b'202', b'202'), (b'301', b'301'), (b'302', b'302'), (b'311', b'311')]),
        ),
    ]
