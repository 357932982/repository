from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^list(?P<type>\d+)_(?P<sort>\d+)_(?P<index>\d+)/$', views.get_list, name='get_list'),
    url(r'^detail(?P<type>\d+)_(?P<id>\d+)/$', views.detail, name='detail'),
]
