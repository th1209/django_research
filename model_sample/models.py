# -*- coding: utf-8 -*-
u"""モデルクラスをまとめたモジュール。"""

from django.db import models


class Manufacturer(models.Model):
    u"""自動車製造業者を表すモデル。"""

    name = models.CharField(max_length=256)

    def __str__(self):
        u"""このクラスの文字列表現。"""
        return self.name


class Car(models.Model):
    u"""自動車を表すモデル。"""

    name = models.CharField(max_length=256)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        u"""このクラスの文字列表現。"""
        return self.name


class Article(models.Model):
    u"""ブログ記事を表すモデル。"""

    title = models.CharField(max_length=256)
    # 今回はサンプルのため、4,000文字程度とする。
    text = models.TextField(max_length=4096)

    def __str__(self):
        u"""このクラスの文字列表現。"""
        return self.title


class Tag(models.Model):
    u"""ブログ記事を分類するタグ。"""

    name = models.CharField(max_length=256)

    def __str__(self):
        u"""このクラスの文字列表現。"""
        return self.name


class ArticleTag(models.Model):
    u"""ArticleモデルとTagモデルの多対多関係を実現する中間テーブル。"""

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    create_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        u"""このクラスの文字列表現。"""
        return 'Article:' + self.article.title + ' Tag:' + self.tag.name
