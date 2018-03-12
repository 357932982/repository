from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^place_order/$', views.place_order, name='place_order'),
    url(r'^order_handler/$', views.order_handler, name='order_handler'),
]