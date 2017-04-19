from django.conf.urls import include, url
from . import views

#http://stackoverflow.com/questions/25907719/noreversematch-exception-redirect-with-keyword-arguments

urlpatterns =[
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
