# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weibostatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weibo_id', models.CharField(max_length=30, verbose_name=b'weibo_id')),
                ('screen_name', models.CharField(max_length=30, verbose_name=b'screen_name')),
                ('uid', models.CharField(max_length=30, verbose_name=b'uid')),
                ('date_published', models.DateTimeField(verbose_name=b'date_published')),
                ('context', models.CharField(max_length=1024, verbose_name=b'context')),
            ],
        ),
    ]
