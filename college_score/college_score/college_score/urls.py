from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
	#main view of the app 
#	(r'^test/',include('test.urls')),
	#used for autocomplete
#	(r'^getnames/', include('getnames.urls')),
	#this view is activated when the user has entered none or unfound values
#	(r'^fail/', include('fail.urls')),
        #define the admin url
        (r'^admin/', include(admin.site.urls)),
	)



## have to define the rest of the urls once they are workign fine.
