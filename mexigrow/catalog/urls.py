from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login-user/$', views.login_buildout, name='login-user'),
    re_path(r'^reg/$', views.reg, name='reg'),
    re_path(r'^logout-user/$', views.logout_buildout, name='logout-user'),
    re_path(r'^bid/$', views.bid, name='bid'),
    
    
    re_path(r'^proyects/$', views.ProyectListView.as_view(), name='proyects'),
    re_path(r'^proyect/(?P<pk>\d+)$', views.ProyectDetailView.as_view(), name='proyect-detail'),
    
    re_path(r'^myinvestments/$', views.OwnedProyectsByUserListView.as_view(), name='my-investments'),
    re_path(r'^myinvestment/(?P<pk>\d+)$', views.OwnedProyectsByUserDetailView.as_view(), name='my-investment'),
    
    re_path(r'^proyect/create/$', views.ProyectCreate.as_view(), name='proyect_create'),
    re_path(r'^proyect/(?P<pk>\d+)/update/$', views.ProyectUpdate.as_view(), name='proyect_update'),
    re_path(r'^proyect/(?P<pk>\d+)/delete/$', views.ProyectDelete.as_view(), name='proyect_delete'),
    
    re_path(r'^investment/create/$', views.ProyectInstanceCreate.as_view(), name='proyectinstance_create'),
    re_path(r'^investment/(?P<pk>\d+)/update/$', views.ProyectInstanceUpdate.as_view(), name='proyectinstance_update'),
    re_path(r'^investment/(?P<pk>\d+)/delete/$', views.ProyectInstanceDelete.as_view(), name='proyectinstance_delete'),
]