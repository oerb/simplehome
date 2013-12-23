from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Wysiwyg Tool
    url(r'^tinymce/', include('tinymce.urls')),
    # Main Page Url
    url(r'^$', 'blog.views.mainpage', name="mainpage"),
    # Include for the App URL Files
    url(r'^banner/', include('banner.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^menues/', include('menues.urls')),
    # Admin Foo
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
