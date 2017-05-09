from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.indexview.as_view(), name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^home/', views.home, name='home'),
    url(r'^(?P<id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<pk>[0-9]+)/update-de/$', views.updateview.as_view(), name='update_de'),

]
