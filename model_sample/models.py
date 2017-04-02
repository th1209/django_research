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
