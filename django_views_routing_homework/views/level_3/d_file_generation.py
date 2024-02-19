"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

import json
import random
import string

from django.http import HttpRequest, HttpResponse


def generate_text(length: int) -> str:
    text = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    return text


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    lenght = request.GET.get('length', None)
    if lenght is not None:
        try:
            lenght = int(lenght)
            if lenght > 1000 or lenght < 1:
                return HttpResponse(content=json.dumps({}), status=403)
        except ValueError:
            return HttpResponse(content=json.dumps({}), status=403)
        file_content = generate_text(length=lenght)
        response = HttpResponse(
            content=file_content,
            content_type='text/plain',
            headers={'Content-Disposition': 'attachment; filename="file.txt"'},
            status=200,
        )
        return response
    return HttpResponse(status=403, content=json.dumps({}))
