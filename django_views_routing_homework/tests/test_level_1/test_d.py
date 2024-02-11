import pytest


@pytest.mark.parametrize('user_id, expected_response', [
    (1, b'{"username": "red_dev", "age": 34}'),
    (2, b'{"username": "green_bear", "age": 43}'),
    (3, b'{"username": "monster", "age": 17}'),
])
def test__get_user_info_view_success(user_id, expected_response, client):
    response = client.get(f'/user-info/{user_id}/')
    assert response.status_code == 200
    assert response.content == expected_response


def test__get_user_info_view_not_found(client):
    response = client.get('/user-info/999/')
    assert response.status_code == 404
