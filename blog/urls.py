from django.urls import path, re_path
# from django.conf.urls import url, include
from . import views

urlpatterns = [
    path(r'', views.index),
    re_path(r'article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path(r'edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    re_path(r'edit/action/$', views.edit_action, name='edit_action'),
]
