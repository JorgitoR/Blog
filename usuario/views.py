# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login

from .forms import Registrarce, login, registro

from .models import Usuario
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from django.contrib.auth import(

	authenticate,
	get_user_model,
	login,
	logout
)

User = get_user_model()

class Registro(CreateView):
	model         = Usuario
	form_class    = registro
	template_name = 'registration/registrarce.html'

	def get_context_data(self, **kwargs):
		kwargs['titulo'] = 'Unete a Nuestro Blog'
		return super(Registro, self).get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		auth_login(self.request, user)
		return redirect('ListaBlog')

class UsuarioView(DetailView):
	template_name = "Usuario/perfil_publico.html"
	queryset      = User.objects.all()

	def get_object(self):
		return get_object_or_404(User, username__iexact = self.kwargs.get("username"))

