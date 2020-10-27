from django.conf.urls import url 
from django.contrib.auth.views import logout
from django.conf import settings
from django.contrib.auth import views as auth_views


from .views import(

	Registro,
	UsuarioView,

)


urlpatterns = [

	url(r'^Registro/$', Registro.as_view(), name='Registro'),
    url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
 	

	url(r'^(?P<username>[\w.@+-]+)/$', UsuarioView.as_view(), name="usuario_detail"),		
 

]