#!/usr/bin/env python 
#-*- coding:utf-8 -*- 

from django.contrib import admin
from models import *

class BugFixAdmin(admin.ModelAdmin):
    list_display=('name','get_text','createdate','date','status','get_time')
    list_display_links=('name',)
    list_filter=('status','date',)
    ordering=('status','date')

admin.site.register(BugFix,BugFixAdmin)

