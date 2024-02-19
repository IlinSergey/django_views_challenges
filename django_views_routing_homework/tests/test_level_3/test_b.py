import json

import pytest


@pytest.mark.parametrize('data, expected_response', [
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
        "registered_from": "website",
        "age": 34
    }, b'{"is_valid": true}'),
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
        "registered_from": "mobile_app",
        "age": 34
    }, b'{"is_valid": true}'),
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
        "registered_from": "website"
    }, b'{"is_valid": true}'),
])
def test__validate_user_data_view__success(client, data, expected_response):
    result = client.post('/user/validate/', data=json.dumps(data), content_type='application/json')
    assert result.status_code == 200
    assert result.content == expected_response


@pytest.mark.parametrize('data, expected_response', [
    ({
        "full_name": "John",
        "email": "jy8wD@example.com",
        "registered_from": "website",
        "age": 34
    }, b'{"is_valid": false}'),
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
        "registered_from": "uncnown",
        "age": 34
    }, b'{"is_valid": false}'),
    ({
        "full_name": "John Doe",
        "email": "jy8example.com",
        "registered_from": "website",
        "age": 34
    }, b'{"is_valid": false}'),
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
        "registered_from": "website",
        "age": 121
    }, b'{"is_valid": false}'),
])
def test__validate_user_data_view__not_valid_data(client, data, expected_response):
    result = client.post('/user/validate/', data=json.dumps(data), content_type='application/json')
    assert result.status_code == 200
    assert result.content == expected_response


@pytest.mark.parametrize('data', [
    ({
        "full_name": "John",
    }),
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
    }),
    ({
        "full_name": "John Doe",
        "email": "jy8wD@example.com",
        "registered_from": "website",
        "age": 34,
        "extra_field": "extra"
    })
])
def test__validate_user_data_view__not_valid_json(client, data):
    result = client.post('/user/validate/', data=json.dumps(data), content_type='application/json')
    assert result.status_code == 400


def test__validate_user_data_view__not_json(client):
    result = client.post('/user/validate/', data='not_json', content_type='application/json')
    assert result.status_code == 400


def test__validate_user_data_view__not_valid_method(client):
    result = client.get('/user/validate/')
    assert result.status_code == 405
