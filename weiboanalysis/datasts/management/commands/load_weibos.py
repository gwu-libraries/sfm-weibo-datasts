#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import logging
from django.conf import settings
from datasts.models import Weibostatus
from weibo_warc_iter import WeiboWarcIter
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'load weibo status from warc files to analysis statues percents'

    def flush_weibostatus(self):
        """
        Wipe all the exist weibo status in the database.
        So we don't accidentally dupe ourselves.
        """
        #Weibostatus.objects.all().delete()
        print "test"

    def handle(self, *args, **options):
        """
        Load the weibos post from the warc files, adding them to the database.
        """

        self.data_dir = settings.DATA_DIR
        logging.debug("flush weibo status...")
        #self.flush_weibostatus()

        weibo_list = []
        for file in os.listdir(self.data_dir):
            if file.endswith(".warc.gz"):
                path = os.path.join(self.data_dir, file)
                weibo_iter = WeiboWarcIter(path)
                for weibo in weibo_iter:
                    print weibo
                #print file
