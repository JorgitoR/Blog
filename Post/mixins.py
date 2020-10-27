from django import forms
from django.forms.utils import ErrorList

class FormsUserNeedMixin(object):

	def form_valid(self, form):
		if self.request.user.is_authenticated():
			form.instance.usuario = self.request.user
			return super(FormsUserNeedMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Usuario no logeado"])
			return self.form_invalid(form)


class UserOwnerMixin(object):
	def form_valid(self, form):
		if form.instance.usuario == self.request.user:
			return super(UserOwnerMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["No te corresponde"])
			return self.form_invalid(form)


class ProhibidoMixin(object):
	def form_valid(self, form):
		if form.instance.usuario != self.request.user:
			reponse = HttpResponse("You do not have permission to do this.")
			reponse.status_code = 403
			return reponse