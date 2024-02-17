"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут:
 https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

import json
import time

import requests  # type: ignore [import-untyped]
from django.http import HttpRequest, HttpResponse


def get_response_from_github_api(github_username: str) -> dict | None:
    max_retries = 2
    delay_seconds = 0.5
    for _ in range(max_retries):
        try:
            response = requests.get(
                f'https://api.github.com/users/{github_username}'
            )
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except ConnectionError:
            time.sleep(delay_seconds)
        except requests.exceptions.Timeout:
            time.sleep(delay_seconds)
        except requests.exceptions.TooManyRedirects:
            return None
        except requests.exceptions.RequestException:
            return None


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> HttpResponse:
    user_info = get_response_from_github_api(github_username)
    if user_info:
        name = user_info.get('name')
        if name:
            return HttpResponse(content=json.dumps({'name': name}))
        else:
            return HttpResponse(content=json.dumps({'name': None}))
    else:
        return HttpResponse(content=json.dumps({}), status=404)
