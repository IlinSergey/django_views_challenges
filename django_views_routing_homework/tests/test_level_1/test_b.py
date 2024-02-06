import pytest


@pytest.mark.parametrize('url', [
    ('bye'),
    ('bye/'),
])
def test__bye_user_view(url, client):
    response = client.get(f'/{url}')
    assert response.status_code == 200
    assert response.content == b'Bye, user!'
