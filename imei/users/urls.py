from django.conf.urls import url
from django.contrib import admin
from .import views 
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^register/$', views.register_url, name='register_url'),
    url(r'^check/$', views.check_url, name='check_url'),
    
    

]
