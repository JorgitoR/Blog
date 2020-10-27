# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey

from django.conf import settings

class Comentario(models.Model):
	usuario        = models.ForeignKey(settings.AUTH_USER_MODEL)
	texto          = models.TextField(verbose_name="Comentario")
	tiempo         = models.DateTimeField(auto_now_add=True)
	actualizar     = models.DateTimeField(auto_now=True)

	content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id      = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	class Meta:
		ordering = ["-tiempo"]
