from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # URL for Blog Items in Detail
    url(r'^blog/(?P<item_id>\d+)/$', 'blog.views.index', name='blog_item'),
    # Blog Views
    url(r'^l0/(?P<choice_id>\d+)/$', 'blog.views.blog_level0', name='blog_level0'),
    url(r'^l1/(?P<choice_id>\d+)/$', 'blog.views.blog_level1', name='blog_level1'),
)
