# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_auto_20170802_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='winners',
            name='printed',
            field=models.BooleanField(default=False),
        ),
    ]
