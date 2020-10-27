# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.utils.html import escape, mark_safe
from markdown_deux import markdown

from django.contrib.contenttypes.fields import GenericRelation

from usuario.models import Usuario
from comentar.models import Comentario
import re
from tags.signals import pasar_tags

from django.conf import settings

class Categoria(models.Model):
	nombre    = models.CharField(max_length=120)
	color     = models.CharField(max_length=7, default='#007bff')

	def __unicode__(self):
		return self.nombre

	def get_html(self):
		nombre = escape(self.name)
		color  = escape(self.color)
		html   = '<span class="categoria_badge" style="background-color:%s">%s</span>' % (color, name)
		return mark_safe(html)

class BlogManager(models.Manager):

	def like_palanca(self, usuario, blog_obj):
		if usuario in blog_obj.like.all():
			is_liked = False
			blog_obj.like.remove(usuario)
		else:
			is_liked = True
			blog_obj.like.add(usuario)

		return is_liked


class MysInteres(models.Model):
	usuario  = models.OneToOneField(Usuario)
	interes  = models.ManyToManyField(Categoria, related_name="interes")

	def __unicode__(self):
		return self.usuario.username

def crear_interes(sender, instance, created, *args, **kwargs):

	if created:
		interes = MysInteres.objects.get_or_create(usuario=instance)

post_save.connect(crear_interes, sender=Usuario)

class Blog(models.Model):
	usuario   = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='blog')
	categoria = models.ForeignKey(Categoria, blank=True, null=True)
	
	titulo    = models.CharField(max_length=300)
	imagen    = models.ImageField(upload_to="post")
	texto     = models.TextField(verbose_name="descripcion")
	tags      = models.CharField(max_length=120)

	like      = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="liked")

	comentario= GenericRelation(Comentario, related_query_name='comentario')
	slug      = models.SlugField(unique=True, blank=True)
	publicado = models.DateField(verbose_name="Programar publicacion", auto_now=False, auto_now_add=False, null=True)
	actualizar= models.DateTimeField(auto_now=True)
	tiempo    = models.DateTimeField(auto_now_add=True)


	objects = BlogManager()

	def __unicode__(self):
		return self.titulo

	def get_markdown(self):
		texto       = self.texto
		mardown_txt = markdown(texto)
		return mark_safe(mardown_txt)

	def get_absolute_url(self):
		return reverse("blog_detail", kwargs={"slug":self.slug})

	def get_pk_url(self):
		return reverse("test_url", kwargs={"pk":self.pk})



def crear_url(instance, Url=None):

	slug =  slugify(instance.titulo)
	if Url is not None:
		slug = Url

	qs = Blog.objects.filter(slug=slug).order_by("-id")

	if qs.exists():
		nueva_url = "%s-%s"%(slug, qs.first().id)
		return crear_url(instance, Url=nueva_url)

	return slug

def callback_url(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = crear_url(instance)
pre_save.connect(callback_url, sender=Blog)


def tags_receiver(sender, instance, created, *args, **kwargs):
	if created:

		tags_regex = r'#(?P<hashtag>[\w\d-]+)'
		tag = re.findall(tags_regex, instance.tags)
		pasar_tags.send(sender=instance.__class__, tags=tag)

post_save.connect(tags_receiver, sender=Blog)