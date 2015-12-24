from django.conf.urls import patterns, include, url 
 
 #main page is college_score/test. This is the gateway
#If the user enters all the required information , okay
#Else, he goes to the college_score/fail
#the college_score/get_names is used for autocomplete

urlpatterns = patterns('',
	#main view of the app 
	url(r'^test/$','education_score.views.formview'),
	#used for autocomplete
	url(r'^getnames/$', 'education_score.views.getnamesview'),
	#this view is activated when the user has entered none or unfound values
	url(r'^fail/$', 'education_score.views.failview'),
    )
