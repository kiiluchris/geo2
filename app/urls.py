from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^$', views.home, name="home"),
    url(r'^page(?P<id>[0-9]+)/$', views.page, name="page"),
]
