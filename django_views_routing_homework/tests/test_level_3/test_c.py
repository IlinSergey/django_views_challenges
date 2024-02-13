
from unittest.mock import patch

import pytest
import responses

from django_views_routing_homework.views.level_3.c_github_full_name import \
    get_response_from_github_api


def test__get_response_from_github_api__success():
    with patch(
        'django_views_routing_homework.views.level_3.c_github_full_name.requests.get'
            ) as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'name': 'Ilya Lebedev'}
        response = get_response_from_github_api('IlyaLebedev')
        assert response == {'name': 'Ilya Lebedev'}


def test__get_response_from_github_api__not_found():
    with patch(
        'django_views_routing_homework.views.level_3.c_github_full_name.requests.get'
            ) as mock_get:
        mock_get.return_value.status_code = 404
        response = get_response_from_github_api('IlyaLebedev')
        assert response is None


@pytest.mark.parametrize('github_username, expected_name, expected_result', [
    ('IlyaLebedev', 'Ilya Lebedev', b'{"name": "Ilya Lebedev"}'),
    ('red_dev', 'Red Dev', b'{"name": "Red Dev"}'),
])
@responses.activate
def test__fetch_name_from_github_view__success(client, github_username, expected_name, expected_result):
    responses.add(
        responses.GET,
        f'https://api.github.com/users/{github_username}',
        json={'name': expected_name},
        status=200
    )
    response = client.get(f'/user/github/{github_username}/full-name/')
    assert response.status_code == 200
    assert response.content == expected_result


@responses.activate
def test__fetch_name_from_github_view__with_not_name(client):
    responses.add(
        responses.GET,
        'https://api.github.com/users/IlyaLebedev',
        json={'name': None},
        status=200
    )
    response = client.get('/user/github/IlyaLebedev/full-name/')
    assert response.status_code == 200
    assert response.content == b'{"name": null}'


@responses.activate
def test__fetch_name_from_github_view__not_found(client):
    responses.add(
        responses.GET,
        'https://api.github.com/users/IlyaLebedev',
        status=404
    )
    response = client.get('/user/github/IlyaLebedev/full-name/')
    assert response.status_code == 404
    assert response.content == b'{}'
