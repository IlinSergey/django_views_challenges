import pytest


@pytest.mark.parametrize('name, language, status_code, expected_result', [
    ('red_dev', 'en', 200, 'Hello, Red Dev'),
    ('red_dev', 'ru', 200, 'Привет, Red Dev'),
    ('green_bear', 'en', 200, 'Hello, Green Bear'),
    ('green_bear', 'uz', 200, 'Xush kelibsiz, Green Bear'),

])
def test__greet_user_in_different_languages_view(client, name, language, status_code, expected_result):
    response = client.get(f'/greet-user-in-different-languages/{name}/{language}/')
    assert response.status_code == status_code
    assert response.content.decode() == expected_result
