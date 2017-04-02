# -*- coding: utf-8 -*-
u"""ビューの処理をまとめたモジュール。"""

from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from model_sample.models import Manufacturer


def manufacturer_list(request):
    """自動車製造業者一覧を表示する。"""
    manufacturers = Manufacturer.objects.all()
    template = loader.get_template('model_sample/manufacturer_list.html')
    context = {
        'manufacturers': manufacturers,
    }
    return HttpResponse(template.render(context, request))


def car_list(request, manufacturer_id):
    """特定の業者が製造している、自動車一覧を表示する。"""
    try:
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
    except Manufacturer.DoesNotExist:
        raise Http404("Manufacturer does not exist")

    template = loader.get_template('model_sample/car_list.html')
    context = {
        'manufacturer': manufacturer,
    }
    return HttpResponse(template.render(context, request))
