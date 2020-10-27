from django import forms
from .models import Blog, MysInteres
from pagedown.widgets import PagedownWidget

class InteresForm(forms.ModelForm):
	class Meta:
		model  = MysInteres
		fields = ('interes',)
		widgets = {
			'interes': forms.CheckboxSelectMultiple
		}

class CrearBlog(forms.ModelForm):
	texto = forms.CharField(widget=PagedownWidget())
	publicado = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Blog
		fields = [
			'categoria', 
			'titulo', 
			'imagen', 
			'texto', 
			'tags',
			'publicado'

		]

		widgets = {

			'tags':forms.TextInput(

				attrs = {'placeholder':'#Tecnologia Empieza con el #'}
			)

		}