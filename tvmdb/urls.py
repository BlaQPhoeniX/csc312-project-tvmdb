from django.conf.urls import patterns, include, url
from django.contrib.auth.views  import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'tvmdb.views.home', name='home'),
     url(r'^login/', login, {'template_name':'login.html'}, name='login'),
     url(r'^logout/', logout, {'template_name' : 'index.html'}),
     url(r'^register/', 'tvmdb.views.register', name='register'),
     url(r'^profile/', 'tvmdb.views.profile', name='profile'),
     url(r'^ajax/events/', 'mediafollower.views.events'),
     url(r'^ajax/search/', 'mediafollower.views.search'),
     url(r'^ajax/subscribe/(\d+)', 'mediafollower.views.subscribe'),
     url(r'^ajax/unsubscribe/(\d+)', 'mediafollower.views.unsubscribe'),
     url(r'^media/(\d+)', 'mediafollower.views.media'),
     url(r'^media/genre/(\d+)', 'mediafollower.views.media_gen'),
     url(r'^media/$', 'mediafollower.views.media'),
    # url(r'^tvmdb/', include('tvmdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
