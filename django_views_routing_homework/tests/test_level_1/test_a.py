
def test__welcome_user_view__success(client):
    response = client.get('/welcome/')
    assert response.status_code == 200
    assert response.content == b'Hello, user!'


def test__welcome_user_view__redirect(client):
    response = client.get('/welcome')
    assert response.status_code == 301
