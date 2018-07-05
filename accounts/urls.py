from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, { 'template_name': 'accounts/login.html' })
]
