from django.conf.urls import url 

from .views import(
	TagsView,
)

urlpatterns = [
	
	url(r'^tag/(?P<hashtag>.*)/$', TagsView.as_view(), name="tags")

]