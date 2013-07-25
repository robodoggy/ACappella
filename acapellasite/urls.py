from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'acapellasite.views.home', name='home'),
    #url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),

    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^arranger/', include('acapellaapp.urlsarranger')),
    url(r'^', inclde('acapellaapp.urlsguest'))

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
