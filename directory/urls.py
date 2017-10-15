from django.conf.urls import url #4

from . import views #4

urlpatterns = [ #4
    url(r'(?P<provider_pk>\d+)/(?P<driver_pk>\d+)/$', views.driver_detail,name='driver_detail'),
    url(r'(?P<pk>\d+)/$', views.provider_detail, name='provider_detail'),
    url(r'^$', views.provider_list, name='provider_list'), #4
] #4
