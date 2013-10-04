from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sina.views.home', name='home'),
    url(r'^api/$', 'sina.views.api', name='api'),
    url(r'^api/callback/$', 'sina.views.callback', name='callback'),
    url(r'^api/cancel/$', 'sina.views.cancel', name='cancel'),

    # url(r'^sina/', include('sina.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
