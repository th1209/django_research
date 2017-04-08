# -*- coding: utf-8 -*-
"""このアプリケーションの管理ツール設定用モジュール。"""

from django.contrib import admin

from form_sample.models import User

admin.site.register(User)
