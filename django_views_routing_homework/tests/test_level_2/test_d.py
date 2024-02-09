from unittest.mock import patch

import pytest


@pytest.mark.parametrize('username, password, status_code', [
    ('red_dev', 'password123', 200),
    ('sarah_connor', 'terminator2', 200),
    ('any_username', 'any_password', 403),
])
def test__process_authorization_view(client, username, password, status_code):
    with patch('django_views_routing_homework.views.level_2.d_authorization.process_authorization_view.json.loads') as mock_json:
        mock_json.return_value = {'username': username, 'password': password}
        response = client.get('/authorization/')
        assert response.status_code == status_code


def test__process_authorization_view__not_allowed(client):
    response = client.get('/authorization/')
    assert response.status_code == 405
