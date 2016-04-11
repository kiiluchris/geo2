from django.conf.urls import include, url
from django.contrib import admin
import views
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^$', views.home, name="home"),
    url(r'^page(?P<id>[0-9]+)/$', views.page, name="page"),
    url(r'^calendar/$', TemplateView.as_view(template_name='eventhome.html'), name='eventhome'),
    url(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='events'),
    url(r'^swingtime/', include('swingtime.urls')),
]
