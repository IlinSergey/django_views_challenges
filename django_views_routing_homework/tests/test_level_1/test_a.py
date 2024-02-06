
def test__welcome_user_view(client):
    response = client.get('/welcome/')
    assert response.status_code == 200
    assert response.content == b'Hello, user!'
