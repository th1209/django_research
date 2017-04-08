# -*- coding: utf-8 -*-
"""このアプリケーションのURL設定用モジュール。"""

from django.conf.urls import url

from form_sample import views

urlpatterns = [
    # ユーザ登録サンプルページ。
    url(r'^registration/$', views.create_user, name='create_user'),
]
