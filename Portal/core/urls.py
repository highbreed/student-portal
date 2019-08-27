from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
	url('^$', views.home, name='home_page'),
	url(r'^personal_information/$', views.information_update, name='info_update'),
	url(r'^fee_statement/$', views.fees, name='fees_page'),
	url(r'^teaching_timetable/$', views.timetable, name='timetable'),
	url(r'^course_registration/$', views.course, name='course'),
	url(r'^results_slip/$', views.results, name='results'),
	url(r'^requests/$', views.requests, name='requests'),
	url(r'^login/$', views.Login, name='login_page'),
	url(r'^logout', views.Logout, name='logout_page'),
]
