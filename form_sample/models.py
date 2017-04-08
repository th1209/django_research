# -*- coding: utf-8 -*-
u"""モデルクラスをまとめたモジュール。"""

from django.db import models


class User(models.Model):
    u"""ユーザ情報を表すモデル。

    注意:
    実運用上では、Userというモデル名を作るのはナンセンス。
    というのも、Djangoの認証機能において、デフォルトでUserという名称のモデルクラスが用意されているから。
    """

    MALE = 'male'
    FEMALE = 'female'

    email_address = models.EmailField(
        max_length=256,
        help_text='A record determined uniquely by this field.',
        unique=True
    )
    password = models.CharField(
        max_length=256
    )
    first_name = models.CharField(
        max_length=256
    )
    last_name = models.CharField(
        max_length=256
    )
    gender = models.CharField(
        max_length=16,
        help_text='See this module constant.'
    )

    def __str__(self):
        u"""このクラスの文字列表現。"""
        return self.email_address
