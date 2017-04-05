# -*- coding: utf-8 -*-
u"""ビューの処理をまとめたモジュール。"""

from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from model_sample.models import Article
from model_sample.models import ArticleTag
from model_sample.models import Manufacturer
from model_sample.models import Tag


def manufacturer_list(request):
    u"""自動車製造業者一覧を表示する。"""
    manufacturers = Manufacturer.objects.all()
    template = loader.get_template('model_sample/manufacturer_list.html')
    context = {
        'manufacturers': manufacturers,
    }
    return HttpResponse(template.render(context, request))


def car_list(request, manufacturer_id):
    u"""特定の業者が製造している、自動車一覧を表示する。"""
    try:
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
    except Manufacturer.DoesNotExist:
        raise Http404("Manufacturer does not exist")

    template = loader.get_template('model_sample/car_list.html')
    context = {
        'manufacturer': manufacturer,
    }
    return HttpResponse(template.render(context, request))


def article_and_tag_list(request):
    u"""記事とタグの一覧を表示する。"""
    tags = Tag.objects.all()
    articles = Article.objects.all()

    template = loader.get_template('model_sample/article_and_tag_list.html')
    context = {
        'tags': tags,
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))


def article_detail(request, article_id=None):
    u"""記事の詳細を表示する。"""
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    article_tags = ArticleTag.objects.filter(article=article_id)

    template = loader.get_template('model_sample/article_detail.html')
    context = {
        'article': article,
        'article_tags': article_tags,
    }
    return HttpResponse(template.render(context, request))


def tag_detail(request, tag_id=None):
    u"""タグの詳細を表示する。"""
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        raise Http404("Tag does not exist")

    article_tags = ArticleTag.objects.filter(tag=tag_id)

    template = loader.get_template('model_sample/tag_detail.html')
    context = {
        'tag': tag,
        'article_tags': article_tags,
    }
    return HttpResponse(template.render(context, request))
