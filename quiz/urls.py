from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.my_login, name='login'),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^quiz/(?P<pk>[0-9]+)/$', views.quiz, name='quiz'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.question, name='question'),
    url(r'^register/$', views.register, name='register'),
]
