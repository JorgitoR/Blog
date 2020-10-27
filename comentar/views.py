# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View 
from django.views.generic import DeleteView

from django.contrib.contenttypes.models import ContentType 

from Post.models import Blog
from .models import Comentario

import json

from django.http import HttpResponse

@method_decorator([login_required], name='dispatch')
class comentarioBlog(View):
	model = Blog
	def post(self, request, pk):
		obj_model = self.model.objects.get(pk=pk)

		comentario = request.POST.get('comentario')
		try:
			comentario = Comentario.objects.get(
				content_type = ContentType.objects.get_for_model(obj_model),
				object_id    = obj_model.id,
				usuario      = request.user,
				texto        = comentario

			)

			comentario.save()

		except Comentario.DoesNotExist:
			comentar = obj_model.comentario.create(usuario=request.user, texto=comentario)


		return HttpResponse(

			json.dumps({

				"resultado":"Yes",
				"comentario":comentario,
				"usuario": comentar.usuario.username

			}),

            content_type="application/json"

		)



@method_decorator([login_required], name='dispatch')
class ComentarioEliminar(DeleteView):
	model  = Comentario
	template_name = "Comentario/coment_eliminar.html"

	def delete(self, request, *args, **kwargs):
		comentario = self.get_object()
		messages.success(request, 'El comentario %s se elimino con exito', Comentario.texto)
		return super(ComentarioEliminar, self).delete(request, *args, **kwargs)

	def get_queryset(self):
		return self.request.user.comentario.all()


	def get_success_url(self):
		return reverse('blog_detail', kwargs={'slug': self.object.slug})
