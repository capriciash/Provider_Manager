from django.conf.urls import url #4

from . import views #4

urlpatterns = [ #4
    url(r'^$', views.provider_list), #4
] #4
