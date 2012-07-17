from django.conf.urls.defaults import patterns, include, url
from youci.blogs import views
urlpatterns = patterns('',
    (r"^$",'blogs.views.blog_index',{"template_name":"blog/index.html"}),
)