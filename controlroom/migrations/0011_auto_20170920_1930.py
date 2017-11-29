# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlroom', '0010_auto_20170917_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='em_1',
            new_name='em',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='em_num_2',
            new_name='em_num',
        ),
    ]
