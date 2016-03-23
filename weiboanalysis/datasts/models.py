from django.db import models
import logging
import datetime

logger = logging.getLogger(__name__)

# Create your models here.


class Weibostatus(models.Model):
    weibo_id = models.CharField('weibo_id', max_length=30)
    screen_name = models.CharField('screen_name', max_length=30)
    uid = models.CharField('uid', max_length=30)
    date_published = models.DateTimeField('date_published')
    context = models.CharField('context', max_length=1024)
    retweeted_context = models.TextField('retweeted_context', default='', max_length=1024)
    is_retweeted = models.BooleanField(default=False)

    def range_datetime(self, start_date, end_date):
        time_pub = datetime.datetime(year=self.date_published.year,
                                 month=self.date_published.month,
                                 day=self.date_published.day)

        if start_date <= time_pub <= end_date:
            return True
        else:
            return False

    # return the context of the weibo
    def __unicode__(self):
        return self.weibo_id


class PicUrl(models.Model):
    thumbnail_pic = models.CharField('thumbnail_pic', max_length=2083)
    bmiddle_pic = models.CharField('bmiddle_pic', max_length=2083)
    original_pic = models.CharField('original_pic', max_length=2083)
    weibo_status = models.ForeignKey(Weibostatus)

    def __unicode__(self):
        return self.original_pic

