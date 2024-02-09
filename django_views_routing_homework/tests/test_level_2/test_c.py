import pytest

from django_views_routing_homework.views.level_2.c_product_type import PRODUCTS


@pytest.mark.parametrize('type_, status_code, expected_result', [
    (None, 200, PRODUCTS),
    ('electronics', 200, [PRODUCTS[0], PRODUCTS[3], PRODUCTS[8], PRODUCTS[13]]),
    ('clothing', 200, [PRODUCTS[1], PRODUCTS[4], PRODUCTS[9], PRODUCTS[15]]),
    ('books', 200, [PRODUCTS[2], PRODUCTS[7], PRODUCTS[16]]),
    ('groceries', 200, [PRODUCTS[5], PRODUCTS[10], PRODUCTS[17]]),
    ('toys', 200, [PRODUCTS[6], PRODUCTS[11], PRODUCTS[18]]),
])
def test__get_products_view(client, type_, status_code, expected_result):
    if type_:
        url = f'/products/?type={type_}'
    else:
        url = '/products/'
    response = client.get(url)
    assert response.status_code == status_code
    assert response.json() == expected_result
