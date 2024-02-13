"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""

import json

from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed

from django_views_routing_homework.views.level_3.pydantic_model import UserData


def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        if data and (len(data) == 3 or len(data) == 4):
            try:
                UserData(**data)
                return HttpResponse(status=200, content=json.dumps({'is_valid': True}))
            except ValueError:
                return HttpResponse(status=200, content=json.dumps({'is_valid': False}))
        return HttpResponse(status=400)
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])
