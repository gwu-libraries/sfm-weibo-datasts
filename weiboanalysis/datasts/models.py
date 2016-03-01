from django.db import models
import logging

logger = logging.getLogger(__name__)

# Create your models here.


class Weibostatus(models.Model):
    weibo_id = models.CharField('weibo_id', max_length=30)
    screen_name = models.CharField('screen_name', max_length=30)
    uid = models.CharField('uid', max_length=30)
    date_published = models.DateTimeField('date_published')
    context = models.CharField('context', max_length=1024)

    # return the context of the weibo
    def __unicode__(self):
        return self.weibo_id