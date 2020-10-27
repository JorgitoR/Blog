from django.conf.urls import url

from .views import(

	inicio,
	CrearBlog,
	ListaBlog,
	DetailBlog,
	BlogEliminar,
	ActualizarBlog,
	Actualizar_Interes,

	Like,

)

urlpatterns = [
	
	url(r'^$', inicio.as_view(), name="inicio"),
	url(r'^crear_blog/$', CrearBlog.as_view(), name="crear_blog"),
	url(r'^MiPerfil/$', ListaBlog.as_view(), name="ListaBlog"),


	url(r'^Interes/$', Actualizar_Interes.as_view(), name="Interes"),

	url(r'^post/(?P<slug>[-\w]+)/$', DetailBlog.as_view(), name = 'blog_detail'),


	url(r'^post/(?P<pk>\d+)/$', DetailBlog.as_view(), name = 'test_url'),


	url(r'^Actualizar/(?P<pk>\d+)/$', ActualizarBlog.as_view(), name = 'ActualizarBlog'),
	url(r'^Eliminar/(?P<pk>\d+)/$', BlogEliminar.as_view(), name = 'BlogEliminar'),
	url(r'^api/(?P<pk>\d+)/Like/$', Like.as_view(), name="Like"),
	

]