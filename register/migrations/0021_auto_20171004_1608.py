# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0020_auto_20171004_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_userinfo',
            name='college',
            field=models.CharField(max_length=100, null=True, choices=[(b'marca', b'marca'), (b'marca', b'marca')]),
        ),
        migrations.AlterField(
            model_name='paid_userinfo',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
