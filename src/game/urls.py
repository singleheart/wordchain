from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^play', views.PlayView.as_view(), name='play'),
    url(r'^form', views.check_rule, name='form'),
    url(r'^score', views.ScoreView.as_view(), name='score'),
]