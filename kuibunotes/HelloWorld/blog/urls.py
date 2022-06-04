from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^get_search/$', views.get_search),
    url(r'^search_get/$', views.search_get),
    url(r'^post_search/$', views.post_search),
    url(r'^search_post$', views.search_post),


    url(r'^es_search/$', views.es_search),
    url(r'^es_notes/$', views.es_notes),
    url(r'^es_notes_search$', views.es_notes_search),
    url(r'^es_handle/$', views.es_handle),
    url(r'^es_insert/$', views.es_insert),
    url(r'^es_delete/$', views.es_delete),
    url(r'^es_update/$', views.es_update),
    url(r'^read/$', views.read),


    url(r'^music/$', views.music),
    url(r'^uploadFile/$', views.uploadFile),
    url(r'^uploadjpg/$', views.uploadjpg),
    url(r'^album/$', views.album),

    url(r'robchat', views.chat),
    url(r'^answer/$', views.answer),



    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^check_register/$', views.check_register),


]
