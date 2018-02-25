from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^register_handler$', views.register_handler, name='register_handler'),
    url(r'^user_name_validate/$', views.user_name_validate, name='user_name_validate'),
]
