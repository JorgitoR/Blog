# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .mixins import FormsUserNeedMixin, UserOwnerMixin, ProhibidoMixin

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
								UpdateView
								)

from .forms  import CrearBlog, InteresForm
from .models import Blog, MysInteres

from django.urls import reverse, reverse_lazy

from django.utils import timezone
import json
from django.http import HttpResponse

class inicio(ListView):
	model               = Blog
	ordering            = ("titulo",)
	context_object_name = 'lista'
	template_name       = 'inicio.html'

	def get_context_data(self, *args, **kwargs):
		context = super(inicio, self).get_context_data()
		context["hoy"] = timezone.now().date()
		return context

	def get_queryset(self):
		if self.request.user.is_authenticated:
			usuario = self.request.user.mysinteres
			interes = usuario.interes.values_list('pk', flat=True)
			queryset= Blog.objects.filter(categoria__in=interes)
			return queryset
		else:

			qs = Blog.objects.all()
			return qs

@method_decorator([login_required], name='dispatch')
class Actualizar_Interes(UserOwnerMixin, UpdateView):
	model         = MysInteres
	form_class    = InteresForm
	template_name = 'Blog/Interes.html'
	success_url   = reverse_lazy('inicio')

	def get_object(self):
		return self.request.user.mysinteres

	def form_valid(self, form):
		messages.success(self.request, 'Interes Actualizado Con Exito')
		return super(Actualizar_Interes, self).form_valid(form)


 
class DetailBlog(DetailView):
    model             = Blog
    template_name     = "Blog/detail_blog.html"
    slug_url_kwarg    = 'slug'
    query_pk_and_slug = True



class ListaBlog(ListView):
	model               = Blog
	ordering            = ("titulo",)
	context_object_name = 'blogs'
	template_name       = 'Blog/Listas.html'

	
	def get_context_data(self, *args, **kwargs):
		context = super(ListaBlog, self).get_context_data()
		context["hoy"] = timezone.now().date()
		return context

	def get_queryset(self):
		queryset = self.request.user.blog \
			.select_related('categoria')
		return queryset

@method_decorator([login_required], name='dispatch')
class CrearBlog(CreateView):
	model         = Blog	
	form_class    = CrearBlog
	template_name = 'Blog/crear.html'

	def form_valid(self, form):
		blog         = form.save(commit=False)
		blog.usuario = self.request.user
		blog.save()
		messages.success(self.request, 'El Blog fue creado exitosamente')
		return redirect('ListaBlog')


@method_decorator([login_required], name='dispatch')
class ActualizarBlog(UserOwnerMixin, UpdateView):
	model               = Blog
	fields              = ('titulo', 'imagen', 'texto', 'tags')
	context_object_name = 'blog'
	template_name       = 'Blog/actualizar.html'

	def get_queryset(self):
		''' 
		Este método es una gestión de permisos implícita a nivel de objeto.
        Esta vista solo coincidirá con los ID de los cuestionarios existentes que pertenecen
        al usuario que ha iniciado sesión.
		'''
		return self.request.user.blog.all()

	def get_success_url(self):
		messages.success(self.request, 'Blog Actualizado Con Exito')
		return reverse('blog_detail', kwargs={'slug': self.object.slug})

@method_decorator([login_required], name='dispatch')
class BlogEliminar(ProhibidoMixin, DeleteView):
	model  = Blog
	context_object_name ="blog"
	template_name = "Blog/blog_eliminar.html"
	success_url = reverse_lazy('ListaBlog')

	def delete(self, request, *args, **kwargs):
		blog = self.get_object()
		if blog.usuario != self.request.user:
			reponse = HttpResponse("You do not have permission to do this.")
			reponse.status_code = 403
			return reponse
		messages.success(request, 'El blog %s se elimino con exito', blog.titulo)
		return super(BlogEliminar, self).delete(request, *args, **kwargs)

	def get_queryset(self):
		return self.request.user.blog.all()


@method_decorator([login_required], name='dispatch')
class Like(View):
	def get(self, request, pk, *args, **kwargs):
		blog_qs = Blog.objects.filter(pk=pk)
		if request.user.is_authenticated():

			is_liked = Blog.objects.like_palanca(request.user, blog_qs.first())
			
			return HttpResponse(

				json.dumps({

					"Yes": "Yes",
					"liked": is_liked

					}),

        		content_type="application/json"

			)