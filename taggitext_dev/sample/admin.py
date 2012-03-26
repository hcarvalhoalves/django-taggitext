# coding: utf-8
from django.db import models
from django.contrib import admin

from models import Page


class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
