# -*- coding: utf-8 -*-
from django import forms
from .models import Usuario

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django.contrib.auth import(

	authenticate,
	get_user_model,
	login,
	logout
)

User = get_user_model()

class registro(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model =  Usuario

	def save(self, commit=True):
		user = super(registro, self).save(commit=False)
		if commit:
			user.save()
		return user 


class login(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':"Usuario"
		}))
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)

			if not user:
				raise forms.ValidationError("Este Usuario No Existe")
			if not user.check_password(password):
				raise forms.ValidationError("Contraseña Incorrecta")
			if not user.is_active:
				raise forms.ValidationError("Este Usuario No Esta Activo")

		return super(login, self).clean(*args, **kwargs)

class Registrarce(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User

		fields = [

			"username",
			"email",
			"password"

		]

		widgets = {

			'username':forms.TextInput(

				attrs = {'placeholder':'Nombre de Usuario'}
			)

		}

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")

		usuarioQs= User.objects.filter(username=username)

		if usuarioQs.exists():

			raise forms.ValidationError("Este usuario ya existe")

		return super(Registrarce, self).clean(*args, **kwargs)