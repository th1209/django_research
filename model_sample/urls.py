# -*- coding: utf-8 -*-
"""このアプリケーションのURL設定用モジュール。"""

from django.conf.urls import url

from model_sample import views

urlpatterns = [
    # 多対一サンプル
    url(r'^many_to_one/manufacturer_list/$', views.manufacturer_list, name='manufacturer_list'),
    url(r'^many_to_one/car_list/(?P<manufacturer_id>\d+)/$', views.car_list, name='car_list'),
]
