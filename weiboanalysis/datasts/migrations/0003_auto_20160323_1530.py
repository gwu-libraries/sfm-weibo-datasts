# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasts', '0002_picurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibostatus',
            name='is_retweeted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weibostatus',
            name='retweeted_context',
            field=models.TextField(default=b'', max_length=1024, verbose_name=b'retweeted_context'),
        ),
    ]
