from django.conf.urls            import patterns, include, url
from django.views.generic.simple import direct_to_template
import os


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')


urlpatterns = patterns('',
    
    ## media
    
    url(r'^site_media/(?P<path>.*)$',                   
         'django.views.static.serve'),
    
    ## polls
   
    url(r'^polls/', include('polls.urls', namespace="polls")),
    
    url(r'^$',                                           
        direct_to_template, {"template": "index.html"}),
    
    ## dojo_ex

    url(r'^dojo_ex/', include('dojo_ex.urls')),

    ## bookmarks
    
    url(r'^bookmarks/$', 
         'bookmarks.views.index'),
    
    url(r'^bookmarks/user/(\w+)/$',                     
         'bookmarks.views.user_page'),
                       
    url(r'^bookmarks/save/$',
         'bookmarks.views.bookmark_save'),
                       
    url(r'^bookmarks/tag/([^\s]+)/$', 
         'bookmarks.views.tag_page'),
                       
    url(r'^bookmarks/tag/$', 
         'bookmarks.views.tag_cloud_page'),
    
    url(r'^bookmarks/search/$',
         'bookmarks.views.search_page'),

    ## bookmarks.login
    
    url(r'^bookmarks/login/$',                          
         'django.contrib.auth.views.login'),
    
    url(r'^bookmarks/logout/$',                         
         'bookmarks.views.logout_page'),
    
    ## bookmarks.register
    
    url(r'^bookmarks/register/$', 
         'bookmarks.views.register_page'),
    
    url(r'^bookmarks/register/success/$', 
        direct_to_template, { 'template': 'registration/register_success.html' }),
    
    ## bookmarks.change_password
                       
    url(r'^bookmarks/account/change_password/$',        
        'django.contrib.auth.views.password_change'),
    
    url(r'^bookmarks/account/change_password/done/$',   
         'django.contrib.auth.views.password_change_done'),
    
    # bookmarks.recovery_password
                      
     url(r'^bookmarks/account/password/reset/$',
          'django.contrib.auth.views.password_reset'), 
    
     url(r'^bookmarks/account/password/sent/$', 
          'django.contrib.auth.views.password_reset_done'), 
                       
     url(r'^bookmarks/account/password/reseted/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
          'django.contrib.auth.views.password_reset_confirm'),
                       
     url(r'^bookmarks/account/password/reset/done/$', 
          'django.contrib.auth.views.password_reset_complete'), 
                       
    # Examples:
    # url(r'^$', 'mercurio.views.home', name='home'),
    # url(r'^mercurio/', include('mercurio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^admin/', 
        include(admin.site.urls)),
)
