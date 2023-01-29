import pytest
from faker import Faker

fake = Faker()
Faker.seed(6174)


@pytest.fixture(name="fake")
def fixture_fake():
    """Pass a seeded Faker instance as a fixture"""
    return fake
