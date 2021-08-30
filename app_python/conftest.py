import pytest
from src import create_app


@pytest.fixture
def client():
    yield create_app().test_client()
