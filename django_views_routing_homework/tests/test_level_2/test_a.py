import pytest


@pytest.mark.parametrize('username, status_code, expected_json', [
    ('red_dev', 200, {'id': 1, 'age': 34}),
    ('green_bear', 200, {'id': '2', 'age': 43}),
    ('monster', 200, {'id': '3', 'age': 17}),
    ('any_username', 404, {'error': 'There is no user info'}),
    ])
def test__get_user_info_by_username_view__success(client, username, status_code, expected_json):
    response = client.get(f'/user-info-by-username/{username}/')
    assert response.status_code == status_code
    assert response.json() == expected_json
