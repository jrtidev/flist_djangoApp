from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login

urlpatterns=[
	url(r'^$', views.home),
	url(r'^addguest/$', views.addGuest),
	url(r'^additem/$', views.addItem),
	url(r'^addguest/(&P<pk>)/$', views.addGuest),
	url(r'^sendmessage/$', views.sendMessage),
	url(r'^registration/$', views.addAccount),
	url(r'^login/$', login, {'template_name': 'main/login.html'})
]