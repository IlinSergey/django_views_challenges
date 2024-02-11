import pytest


@pytest.mark.parametrize('name, language, status_code, expected_result', [
    ('red_dev', 'en', 200, 'Hello, Red_Dev'),
    ('red_dev', 'ru', 200, 'Привет, Red_Dev'),
    ('green_bear', 'en', 200, 'Hello, Green_Bear'),
    ('green_bear', 'uz', 200, '👋, Green_Bear'),

])
def test__greet_user_in_different_languages_view__success(client, name, language, status_code, expected_result):
    response = client.get(f'/greet/{name}/{language}/')
    assert response.status_code == status_code
    assert response.content.decode() == expected_result
