# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail_pic', models.CharField(max_length=2083, verbose_name=b'thumbnail_pic')),
                ('bmiddle_pic', models.CharField(max_length=2083, verbose_name=b'bmiddle_pic')),
                ('original_pic', models.CharField(max_length=2083, verbose_name=b'original_pic')),
                ('weibo_status', models.ForeignKey(to='datasts.Weibostatus')),
            ],
        ),
    ]
