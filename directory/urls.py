from django.conf.urls import url #4
from django.core.urlresolvers import reverse

from . import views #4

urlpatterns = [ #4
    url(r'(?P<provider_pk>\d+)/(?P<driver_pk>\d+)/$', views.driver_detail, name='driver_detail'),
    url(r'(?P<provider_pk>\d+)/add_driver/$', views.add_driver, name='add_driver'),
    url(r'(?P<pk>\d+)/$', views.provider_detail, name='provider_detail'),
    url(r'^defensive_driving/$', views.ddriving_list, name='ddriving_list'),
    url(r'^pass/$', views.pass_list, name='pass_list'),
    url(r'^drivers/$', views.driver_list, name='driver_list'),
    url(r'^trainings/$', views.training_nav, name='training_nav'),
    url(r'^providers/$', views.provider_list, name='provider_list'),
    url(r'^$', views.dashboard, name='dashboard'), #4
] #4
