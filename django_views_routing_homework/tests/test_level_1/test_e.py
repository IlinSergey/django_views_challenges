import pytest

from django_views_routing_homework.views.level_1.e_month_title import \
    get_month_title_by_number


@pytest.mark.parametrize('month_number, expected_result', [
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (10, 'October'),
])
def test__month_title_by_number(month_number, expected_result):
    assert get_month_title_by_number(month_number) == expected_result


@pytest.mark.parametrize('month_number, expected_response', [
    (1, b'January'),
    (2, b'February'),
    (3, b'March'),
])
def test__get_month_title_view_success(month_number, expected_response, client):
    response = client.get(f'/month-title/{month_number}/')
    assert response.status_code == 200
    assert response.content == expected_response


@pytest.mark.parametrize('month_number', [
    0,
    13,
])
def test__get_month_title_view_not_found(month_number, client):
    response = client.get(f'/month-title/{month_number}/')
    assert response.status_code == 404
    assert response.content == 'Месяца с таким номером не существует'.encode('utf-8')
