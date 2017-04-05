## モデル作成用のスクリプトについて

* `python manage.py shell`で、コンソールを立ち上げる。
* スクリプトを書いて、DBにデータを保存する。
* git上には、sqliteのバイナリデータをコミットすれば、データの保存は完了。
* データの作成に再現性を持たせたい場合、manage.pyのdumpdataオプションでデータを吐き出しておくと良い。
  * `python manage.py dumpdata model_sample --indent 4 --format yaml`

### 多対一データ作成例

```python
from model_sample.models import Manufacturer, Car

# 自動車製造会社レコードの生成。
manufacturers = []
manufacturer.append(Manufacturer.objects.create(name="toyota"))
manufacturer.append(Manufacturer.objects.create(name="nissan"))
manufacturer.append(Manufacturer.objects.create(name="honda"))
for manufacturer in manufacturers:
    manufacturer.save()

# 以下のような関数を定義して...
def create_car_records(manufacturer, car_names):
    for car_name in car_names:
        car = Car.objects.create(name=car_name,manufacturer=manufacturer)
        car.save()

# 自動車レコードをまとめて生成する。
from model_sample.models import Car
create_car_records(manufacturers[0], ['prius', 'vits', 'c-hr'])
create_car_records(manufacturers[1], ['serena', 'note', 'x-trail', 'roox'])
create_car_records(manufacturers[2], ['freed', 'nsx', 'n-wgn'])

# 確認。
for manufacturer in manufacturers:
    print(manufacturer.car_set.all())
```

### 多対多データ作成例

```python
from model_sample.models import Article, Tag, ArticleTag

# 事前に以下の関数を定義する(多対多では、bulk_createが使えない!)
def create_model_in_bulk(models):
    for model in models:
        model.save()
    return models

# Acticleレコードをまとめて作成する。
# Article.objects.bulk_create([
#     Article(title='Django Tutorial', text='This article explain Django basic modules...'),
#     Article(title='SQLite Commands', text='This article explain SQLite basic commands...'),
#     Article(title='MySql datatype', text='This article explain MySql datatype...'),
# ])
articles = create_model_in_bulk([
    Article(title='Django Tutorial', text='This article explain Django basic modules...'),
    Article(title='SQLite Commands', text='This article explain SQLite basic commands...'),
    Article(title='MySql datatype', text='This article explain MySql datatype...'),
])

# Tagレコードをまとめて作成する。
tags = create_model_in_bulk([
    Tag(name='programming'),
    Tag(name='python'),
    Tag(name='database'),
    Tag(name='sqlite'),
    Tag(name='mysql'),
])

# 中間テーブルを作成する。
article_tags = []
# Djangoの記事にタグを貼る。
article_tags.append(ArticleTag.objects.create(article=articles[0] , tag=tags[0]))
article_tags.append(ArticleTag.objects.create(article=articles[0] , tag=tags[1]))
article_tags.append(ArticleTag.objects.create(article=articles[0] , tag=tags[2]))
# SQLiteの記事にタグを貼る。
article_tags.append(ArticleTag.objects.create(article=articles[1] , tag=tags[2]))
article_tags.append(ArticleTag.objects.create(article=articles[1] , tag=tags[3]))
# MySqlの記事にタグを貼る。
article_tags.append(ArticleTag.objects.create(article=articles[2] , tag=tags[2]))
article_tags.append(ArticleTag.objects.create(article=articles[2] , tag=tags[4]))
```