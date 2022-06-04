from django.conf.urls import url
from article import views
urlpatterns = [
    url(r'^hello/$', views.hello),
]
