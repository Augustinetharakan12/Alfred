# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_paid_userinfo_paid_winners'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_userinfo',
            name='printed',
            field=models.BooleanField(default=False),
        ),
    ]
