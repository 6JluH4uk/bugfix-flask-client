#-*- coding:utf-8 -*- 

from django.db import models
from django.conf import settings

class BugFix(models.Model):
    name = models.CharField(verbose_name = u'Название задачи', max_length = 1000, help_text = u'Уникальное название задачи для ее быстрой идентификации')
    text = models.TextField(verbose_name = u'Описание', blank = True, null = True, help_text = u'Подробное описание задачи')
    date = models.DateField(verbose_name = u'Срок', null = True, blank = True, help_text = u'К какому числу задача должна быть выполнена')
    choices = ((u'0', u'Поставлена'),
               (u'1', u'Проверка'),
               (u'2', u'Отменена'),
               (u'3', u'Выполнена'),
               (u'4', u'Удалена'), )
    status = models.CharField(verbose_name = u'Статус', max_length = 255, blank = True, choices = choices, help_text = u'Статус задачи')
    timefj = models.TimeField( verbose_name = u'Время на работу', blank = True, null = True, help_text = u'Выберите время затраченное на работу', default = '00:00:00')
    createdate = models.DateField(verbose_name = u'Дата создания', auto_now_add = True)

    def to_dict(self):
        return {'name':       self.name,
                'text':       self.text,
                'date':       str(self.date),
                'status':     self.status,
                'createdate': str(self.createdate)}

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
        if hasattr(settings, 'BUGFIX_URL') and hasattr(settings, 'BUGFIX_PROJECT'):
            import urllib2, json
            data = {'json': [bug.to_dict() for bug in BugFix.objects.all()], 'project': settings.BUGFIX_PROJECT}
            jsn = json.dumps(data)
            req = urllib2.Request(settings.BUGFIX_URL, jsn, headers={'Content-Type': 'application/json'})
            try:
                urllib2.urlopen(req)
            except:
                pass

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Задачи"
        verbose_name = u"Задачу"
