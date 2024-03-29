from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from youci import views
from youci import blogs
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogsystem.views.home', name='home'),
    # url(r'^blogsystem/', include('blogsystem.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    (r'^$','youci.views.homepage'),
    (r"^blog/",include("blogs.urls")),
    (r"^test/$",views.test),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)
