from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^experience/$', views.experience, name='experience'),
	url(r'^projects/$', views.projects, name='projects'),
	url(r'^blog/$', views.blog, name='blog')
]