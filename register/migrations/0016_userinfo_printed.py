# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_winners_printed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='printed',
            field=models.BooleanField(default=False),
        ),
    ]
