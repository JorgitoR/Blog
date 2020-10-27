# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Blog, Categoria, MysInteres

admin.site.register(Categoria)
admin.site.register(Blog)
admin.site.register(MysInteres)