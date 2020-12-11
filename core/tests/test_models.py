import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestDeck:
    def test_simple(self):
        assert 1 == 1, 'Should create deck instance'