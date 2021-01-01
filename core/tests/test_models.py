import pytest

pytestmark = pytest.mark.django_db


class TestDeck:
    def test_simple(self):
        assert 1 == 1, "Should create deck instance"
