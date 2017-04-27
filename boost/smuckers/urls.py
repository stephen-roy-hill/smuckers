from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^display-data/$', views.display, name='display'),
    url(r'^enter-data/$', views.enter, name='enter'),
    url(r'^login/$', views.loginUser, name='loginuser'),
    url(r'^loginpost/$', views.loginPost, name='loginpost'),
    url(r'^logout/$', views.logoutUser, name='logout'),
]