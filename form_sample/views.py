# -*- coding: utf-8 -*-
u"""ビューの処理をまとめたモジュール。"""

from django.shortcuts import render

from form_sample.forms import UserForm
from form_sample.models import User


def create_user(request):
    u"""フォームによる、ユーザレコードの作成を行う。"""
    if request.method == 'POST':
        # POSTによりデータ送信された場合。
        form = UserForm(request.POST)

        # 各種チェックを実施して、駄目ならフォームページへ。
        if not form.is_valid():
            return render(
                request,
                'form_sample/registration_form.html',
                dict(form=form, message='form validation error.'),
            )
        if form.cleaned_data['password_1'] != form.cleaned_data['password_2']:
            return render(
                request,
                'form_sample/registration_form.html',
                dict(form=form, message='incorrect password.'),
            )
        if User.objects.filter(email_address=form.cleaned_data['email_address']).exists():
            return render(
                request,
                'form_sample/registration_form.html',
                dict(form=form, message='user record already exists.'),
            )

        # Userレコードを生成。
        user = User.objects.create(
            email_address=form.cleaned_data['email_address'],
            password=form.cleaned_data['password_1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            gender=form.cleaned_data['gender'],
        )
        user.save()

        # フォーム入力画面へ遷移。
        return render(
            request,
            'form_sample/registration_completion.html',
            dict(message='registration completed.'),
        )
    else:
        # 空の入力フォームを表示する場合。
        form = UserForm()
        return render(
            request,
            'form_sample/registration_form.html',
            dict(form=form),
        )
