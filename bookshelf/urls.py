from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookshelf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('mercator.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<url>.*/)$', include('django.contrib.flatpages.urls')),
)
