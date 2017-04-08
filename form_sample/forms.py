# -*- coding: utf-8 -*-
u"""フォームに関するクラスをまとめたモジュール。"""

from django import forms

from form_sample.models import User


class UserForm(forms.Form):
    u"""Userを作成するためのフォーム。"""

    email_address = forms.EmailField(
        label='email:',
        max_length=256,
    )
    password_1 = forms.CharField(
        label='password:',
        max_length=256,
        widget=forms.PasswordInput,
    )
    password_2 = forms.CharField(
        max_length=256,
        widget=forms.PasswordInput,
    )
    first_name = forms.CharField(
        label='first name:',
        max_length=256
    )
    last_name = forms.CharField(
        label='last name:',
        max_length=256
    )
    # ChoiceFieldの概要については、以下URLを参照すること。
    # https://docs.djangoproject.com/ja/1.11/ref/models/fields/#field-choices
    gender = forms.ChoiceField(
        label='gender:',
        widget=forms.Select,
        choices=(
            (User.MALE, 'male'),
            (User.FEMALE, 'female'),
        )
    )
