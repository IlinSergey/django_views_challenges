def test__bye_user_view__success(client):
    response = client.get('/bye/')
    assert response.status_code == 200
    assert response.content == b'Bye, user!'


def test__bye_user_view__redirect(client):
    response = client.get('/bye')
    assert response.status_code == 301
