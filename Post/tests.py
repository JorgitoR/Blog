# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog

User = get_user_model()

class BlogModelTestCase(TestCase):
	def setUp(self):

		usuarios_aleatorios = User.objects.create(username='jorconmpreki')

	def test_blog_item(self):
		obj = Blog.objects.create(

			usuario = User.objects.first(),
			titulo ='Algunos blogs usuarios_aleatorios'

			)
		self.assertTrue(obj.titulo == 'Algunos blogs usuarios_aleatorios')
		self.assertTrue(obj.id == 1)
		#self.assertEqual(obj.id, 1)
		absolute_url = reverse("test_url", kwargs={"pk":1})
		self.assertEqual(obj.get_pk_url(), absolute_url)


	def blog_test_url(self):

		obj = Blog.objects.create(

			user=User.objects.first(),
			titulo = 'Algunos contenidos'

			)

		absolute_url = reverse("test_url", kwargs={'slug': obj.slug})
		self.assertEqual(obj.get_pk_url(), absolute_url)