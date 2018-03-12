from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^add_(?P<id>\d+)_(?P<count>\d+)/$', views.add, name='add'),
    url(r'^change/$', views.change, name='change'),
    url(r'^delete/$', views.delete, name='delete'),
]
