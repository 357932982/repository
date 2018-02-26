from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handler/$', views.login_handler, name='login_handler'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handler/$', views.register_handler, name='register_handler'),
    url(r'^user_name_validate/$', views.user_name_validate, name='user_name_validate'),
    url(r'^info/$', views.info, name='info'),
    url(r'^order/$', views.order, name='order'),
    url(r'^site/$', views.site, name='site'),
]
