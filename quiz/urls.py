from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.my_logout, name='logout'),
]