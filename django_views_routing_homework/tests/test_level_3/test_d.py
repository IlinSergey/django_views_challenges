import pytest

from django_views_routing_homework.views.level_3.d_file_generation import \
    generate_text


class TestGenerateText:
    @pytest.mark.parametrize('length', [
        100,
        1000,
        50,
    ])
    def test__generate_text(self, length):
        text = generate_text(length)
        assert len(text) == length


class TestGenerateFileWithTextView:
    @pytest.mark.parametrize('length', [
        10,
        100,
        999,
        1000,
    ])
    def test__generate_file_with_text_view__success(self, client, length):
        response = client.get('/text/generate/', {'length': length})
        assert response.status_code == 200
        assert response['Content-Disposition'] == 'attachment; filename="file.txt"'
        assert response['Content-Type'] == 'text/plain'

    @pytest.mark.parametrize('length', [
        1001,
        5000,
        0,
    ])
    def test__generate_file_with_text_view__bad_length(self, client, length):
        response = client.get('/text/generate/', {'length': length})
        assert response.status_code == 403
        assert response.content == b'{}'

    def test__generate_file_with_text_view__not_length(self, client):
        response = client.get('/text/generate/')
        assert response.status_code == 403
        assert response.content == b'{}'

    def test__generate_file_with_text_view__not_integer(self, client):
        response = client.get('/text/generate/', {'length': 'string'})
        assert response.status_code == 403
        assert response.content == b'{}'
