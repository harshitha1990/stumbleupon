from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stumbleproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signin/', 'signin.views.signinForm', name='signinForm'),
    url(r'^test/', 'signin.views.test', name='test'),
    url(r'^addLinks/', 'events.views.addView', name='addLinks'),
    url(r'^admin/', include(admin.site.urls)),
)
