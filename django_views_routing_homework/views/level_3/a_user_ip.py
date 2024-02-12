"""
В этом задании вам нужно реализовать вьюху, которая возвращает IP входящего запроса в виде строки.

Вот тут есть информация о том, как узнать IP:
https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.META
"""

from django.http import HttpRequest, HttpResponse


def show_user_ip_view(request: HttpRequest) -> HttpResponse:
    user_ip = request.META.get('REMOTE_ADDR', 'UNKNOWN')
    return HttpResponse(user_ip)
