
* 以下に、view上でのフォームの簡単な扱い方の例を示す。
* 対話環境を開いて実行してみよう。

```python
>>> from form_sample.forms import UserForm
>>> from django.http import QueryDict

# コンソール環境では、QueryDictオブジェクトによる
# フォームの初期化がやりやすい。
>>> query_dict = QueryDict('email_address=hoge.1234@gmail.com&password_1=1234&password_2=1234&first_name=toshiki&last_name=hata&gender=male', mutable=True)
>>> form = UserForm(query_dict)

# フォームのバリデーション。
>>> form.is_valid()

# バリデーション後は、cleaned_dataプロパティで値が取れる。
# エラーの場合でも、バリデーションに成功したプロパティは取得可能。
>>> form.cleaned_data
{'first_name': 'toshiki', 'password_1': '1234', 'gender': 'male', 'password_2': '1234', 'email_address': 'hoge.1234@gmail.com', 'last_name': 'hata'}

# フォームにエラーがあったかどうかは、errorsで確認可能。
# エラーがあった場合、以下のような辞書が返る。
>>> form.errors
{'gender': ['Select a valid choice. male is not one of the available choices.']}
```
