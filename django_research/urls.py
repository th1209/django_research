# -*- coding: utf-8 -*-
"""プロジェクト全体のURL設定用モジュール。"""

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^model_sample/', include('model_sample.urls', namespace='model_sample')),
    url(r'^form_sample/', include('form_sample.urls', namespace='form_sample')),
]

# 以下、debug-toolbar用の設定。
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
