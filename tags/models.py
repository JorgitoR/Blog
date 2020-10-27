# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.urls import reverse_lazy
from Post.models import Blog
from .signals import pasar_tags

class Tags(models.Model):
	tag    = models.CharField(max_length=120)
	tiempo = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.tag 

	def get_absolute_url(self):
		return reverse_lazy("tags", kwargs={"tags":self.tag})

	def obtener_tags(self):
		return Blog.objects.filter(tags__icontains ='#' + self.tag)


def pasar_tags_receiver(sender, tags, *args, **kwargs):
	if len(tags)>0:
		for tags in tags:
			lista_tags, created = Tags.objects.get_or_create(tag=tags)

pasar_tags.connect(pasar_tags_receiver)