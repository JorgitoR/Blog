from django.conf.urls import url 

from .views import (

	comentarioBlog,
	ComentarioEliminar

)

urlpatterns = [

	url(r'^api/comentario/(?P<pk>\d+)/comentar/$', comentarioBlog.as_view(), name="comentario"),
	url(r'^Eliminar/(?P<pk>\d+)/$', ComentarioEliminar.as_view(), name = 'ComentEliminar'),
]