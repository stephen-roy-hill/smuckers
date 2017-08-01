from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<bol_id>[0-9]+)/displaybol/$', views.displaybol, name='displaybol'),
    url(r'^instructions/$', views.instructions, name='instructions'),
    url(r'^forklift-entry/$', views.forkliftEntry, name='forklift-entry'),
    url(r'^truck-entry/$', views.truckEntry, name='truck-entry'),
    url(r'^display-data/$', views.display, name='display'),
    url(r'^display-manager/$', views.displayManager, name='display-manager'),
    url(r'^display-all/$', views.displayAll, name='display-all'),
    url(r'^(?P<bol_id>[0-9]+)/approvebol/$', views.approvebol, name='approvebol'),
    url(r'^(?P<bol_id>[0-9]+)/unapprovebol/$', views.unapprovebol, name='unapprovebol'),
    url(r'^(?P<bol_id>[0-9]+)/deletebol/$', views.deletebol, name='deletebol'),
    url(r'^(?P<bol_id>[0-9]+)/downloadbol/$', views.downloadbol, name='downloadbol'),
    url(r'^bolpost/$', views.bolPost, name='bolpost'),
    url(r'^bolitempost/$', views.bolItemPost, name='bolitempost'),
    url(r'^enter-data/$', views.enter, name='enter'),
    url(r'^login/$', views.loginUser, name='loginuser'),
    url(r'^loginpost/$', views.loginPost, name='loginpost'),
    url(r'^logout/$', views.logoutUser, name='logout'),
    url(r'^exceltest/$', views.excelTest, name='exceltest'),
]