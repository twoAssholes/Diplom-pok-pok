# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150401_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='other_choice_data',
            field=models.CharField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
