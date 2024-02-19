from unittest.mock import Mock

import pytest

from django_views_routing_homework.views.level_3.a_user_ip import \
    show_user_ip_view


@pytest.mark.parametrize('ip, expected_ip', [
    ('127.0.0.1', b'127.0.0.1'),
    ('89.0.142.86', b'89.0.142.86'),
    ('0.0.0.0', b'0.0.0.0'),
])
def test__show_user_ip_view__success(ip, expected_ip):
    request = Mock()
    request.META = {'REMOTE_ADDR': ip}
    response = show_user_ip_view(request)
    assert response.status_code == 200
    assert response.content == expected_ip


def test__show_user_ip_view__not_ip():
    request = Mock()
    request.META = {}
    response = show_user_ip_view(request)
    assert response.status_code == 200
    assert response.content == b'UNKNOWN'
