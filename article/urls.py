from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^$', views.detail, name = 'detail'),
]
