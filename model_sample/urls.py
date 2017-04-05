# -*- coding: utf-8 -*-
"""このアプリケーションのURL設定用モジュール。"""

from django.conf.urls import url

from model_sample import views

urlpatterns = [
    # 多対一サンプル
    url(r'^many_to_one/manufacturer_list/$', views.manufacturer_list, name='manufacturer_list'),
    url(r'^many_to_one/car_list/(?P<manufacturer_id>\d+)/$', views.car_list, name='car_list'),

    # 多対多サンプル
    url(r'^many_to_many/article_and_tag_list/$', views.article_and_tag_list, name='article_and_tag_list'),
    url(r'^many_to_many/article_detail/(?P<article_id>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^many_to_many/tag_detail/(?P<tag_id>\d+)/$', views.tag_detail, name='tag_detail'),
]
