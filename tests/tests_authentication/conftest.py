import pytest
from faker import Faker
from django.contrib.auth.models import User


@pytest.fixture(name="faker")
def users_factory():
    return Faker()


@pytest.fixture()
def register_user(faker):
    password = faker.password(
        length=12,
    )
    data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password1": password,
        "password2": password,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
    }
    return data


@pytest.fixture
def make_db_user(faker):
    user_data = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password(
            length=12,
        ),
    }
    user = User.objects.create_user(**user_data)
    return {"user": user, "user_data": user_data}


@pytest.fixture()
def make_user_registration(register_user, api_client):
    return api_client.post(
        "/api/auth/register/",
        register_user,
    )
