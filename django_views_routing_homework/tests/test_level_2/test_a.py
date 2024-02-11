import pytest


@pytest.mark.parametrize('username, status_code, expected_json', [
    ('red_dev', 200, {'id': 1, 'age': 34}),
    ('green_bear', 200, {'id': '2', 'age': 43}),
    ('monster', 200, {'id': '3', 'age': 17}),
    ])
def test__get_user_info_by_username_view__success(client, username, status_code, expected_json):
    response = client.get(f'/user-info-by-username/{username}/')
    assert response.status_code == status_code
    assert response.json() == expected_json


def test__get_user_info_by_username_view__not_found(client):
    response = client.get('/user-info-by-username/any_username/')
    assert response.status_code == 404
    assert response.json() == {'error': 'There is no user info'}
