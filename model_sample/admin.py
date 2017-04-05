# -*- coding: utf-8 -*-
"""このアプリケーションの管理ツール設定用モジュール。"""

from django.contrib import admin

from model_sample.models import Article, ArticleTag, Tag

admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(Tag)
