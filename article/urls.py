from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
#    url(r'^(?P<my_args>\d+)/$', views.detail, name = 'detail'),
]
