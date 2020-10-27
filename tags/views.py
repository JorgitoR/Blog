# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from .models import Tags

class TagsView(View):
	def get(self, request, hashtag, *args, **kwargs):
		obj, created  = Tags.objects.get_or_create(tag=hashtag)
		context = {

			"tags":obj 

		}
		return render(request, 'Tags/tag.html', context)