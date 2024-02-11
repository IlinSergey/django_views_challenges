import pytest


@pytest.mark.parametrize('username, expected_response', [
    ('red_dev', b'User banned'),
    ('green_bear', b'User banned'),
    ('monster', b'User banned'),
    ('any_username', b'User not banned'),
    ('sponge_bob', b'User not banned'),

])
def test__is_user_banned_view__success(username, expected_response, client):
    response = client.get(f'/banned/{username}/')
    assert response.status_code == 200
    assert response.content == expected_response
