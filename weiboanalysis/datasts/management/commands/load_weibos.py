#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import datetime
import time
import logging

from django.conf import settings
from datasts.models import Weibostatus
from weibo_warc_iter import WeiboWarcIter
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'load weibo status from warc files to analysis statues percents'

    def created_at_to_dt(self, created_at):
        ts = time.mktime(time.strptime(created_at, '%a %b %d %H:%M:%S +0800 %Y'))
        dt = datetime.datetime.fromtimestamp(ts)
        return timezone.make_aware(dt, timezone.utc)

    def flush_weibostatus(self):
        """
        Wipe all the exist weibo status in the database.
        So we don't accidentally dupe ourselves.
        """
        Weibostatus.objects.all().delete()

    def handle(self, *args, **options):
        """
        Load the weibos post from the warc files, adding them to the database.
        """

        self.data_dir = settings.DATA_DIR
        logging.debug("flush weibo status...")
        self.flush_weibostatus()

        weibo_list = []
        for wfile in os.listdir(self.data_dir):
            if wfile.endswith(".warc.gz"):
                path = os.path.join(self.data_dir, wfile)
                weibo_iter = WeiboWarcIter(path)
                #print path
                for item_type, weibo in weibo_iter:
                    # print weibo["mid"],weibo["user"]["screen_name"].encode("utf-8"),\
                    #    weibo["user"]["id"],weibo["created_at"],weibo["text"].encode("utf-8")
                    # skip the null status
                    if not weibo:
                        continue
                    weibo_row = Weibostatus(weibo_id=weibo["mid"],
                                            screen_name=weibo["user"]["screen_name"],
                                            uid=weibo["user"]["id"],
                                            date_published=self.created_at_to_dt(weibo["created_at"]),
                                            context=weibo["text"])
                    weibo_list.append(weibo_row)

        logger.debug("Loading weibo to database.")
        #print weibo_list[0].uid
        # Batch upload weibo to the database, 200 at a time
        Weibostatus.objects.bulk_create(
            weibo_list,
            batch_size=200
        )
