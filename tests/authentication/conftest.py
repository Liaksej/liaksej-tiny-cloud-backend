import pytest
from faker import Faker


@pytest.fixture
def users_factory():
    return Faker()
