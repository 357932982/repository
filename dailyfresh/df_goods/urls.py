from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^list/$', views.get_list, name='get_list'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^place_order/$', views.place_order, name='place_order'),
]
