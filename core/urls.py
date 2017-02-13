from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns=[
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'main/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'main/logout.html'}),
	url(r'^addguest/$', views.addGuest),
	url(r'^additem/$', views.addItem),
	url(r'^addguest/(&P<pk>)/$', views.addGuest),
	url(r'^sendmessage/$', views.sendMessage),
	url(r'^registration/$', views.addAccount),
	
]