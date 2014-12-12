#-*- coding:utf-8 -*- 

import json
import datetime
from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

class JsonManager(models.Manager):
    def get_json(self):
        myobjects =  super(JsonManager, self).get_query_set()
        bugjson = []
        for o in myobjects:
            name= o.name
            text = o.text.replace("'", "\'").replace('"', '\"')
            date = datetime.date.today()
            if o.date:
                date= o.date.strftime("%d-%m-%Y")
            else:
                date = u'Без даты'
            if o.createdate != '':
                createdate = o.createdate.strftime("%d-%m-%Y")
            else:
                createdate = u'Без даты'
            status = o.get_status_display()
            project = str(Site.objects.all()[0].name)
            bug_id = str(o.id)
            bugjson.append({'name':name, 'text':text, 'date':date, 'createdate':createdate, 'status':status, 'project':project, 'project_bug_id':bug_id})
        return json.dumps(bugjson)


class BugFix(models.Model):
    name = models.CharField(verbose_name = u'Название задачи', max_length = 1000, help_text = u'Уникальное название задачи для ее быстрой идентификации')
    text = models.TextField(verbose_name = u'Описание', blank = True, null = True, help_text = u'Подробное описание задачи')
    date = models.DateTimeField(verbose_name = u'Срок', null = True, blank = True, help_text = u'К какому числу задача должна быть выполнена')
    choices = ((u'0', u'Поставлена'),
               (u'1', u'Проверка'),
               (u'2', u'Отменена'),
               (u'3', u'Выполнена'),
               (u'4', u'Удалена'), )
    status = models.CharField(verbose_name = u'Статус', max_length = 255, blank = True, choices = choices, help_text = u'Статус задачи')
    timefj = models.TimeField( verbose_name = u'Время на работу', blank = True, null = True, help_text = u'Выберите время затраченное на работу', default = '00:00:00')
    createdate = models.DateTimeField(verbose_name = u'Дата создания', auto_now_add = True)

    def get_text(self):
        return self.text
    get_text.short_description = 'Описание'
    get_text.allow_tags = True

    def get_time(self):
        return self.timefj.strftime('%H:%M')
    get_time.short_description = 'Время на работу'
    get_time.allow_tags = True

    def save(self, *args, **kwargs):
        super(BugFix, self).save(*args, **kwargs)
        if hasattr(settings, 'BUGFIX_URL'):
            import urllib, urllib2
            from django.core import serializers
            jsn = serializers.serialize('json', BugFix.objects.all())
            data = urllib.urlencode({'json': jsn })
            urllib2.urlopen(settings.BUGFIX_URL, data)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Задачи"
        verbose_name = u"Задачу"
