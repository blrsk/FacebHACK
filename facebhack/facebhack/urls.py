from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')),
	# url(r'^$', direct_to_template, {"template":"index.html"}, name='index'),
	url(r'^$', TemplateView.as_view(template_name="index.html")),

    
    # Examples:
    # url(r'^$', 'facebhack.views.home', name='home'),
    # url(r'^facebhack/', include('facebhack.foo.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
