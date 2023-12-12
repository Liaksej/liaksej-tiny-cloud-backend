import pytest
from django.contrib.auth.models import User
from faker import Faker


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


@pytest.fixture(scope="function")
def make_db_user(faker):
    def _make_db_user(is_superuser=True):
        user_data = {
            "username": faker.user_name(),
            "email": faker.email(),
            "password": faker.password(
                length=12,
            ),
            "is_staff": is_superuser,
            "is_superuser": is_superuser,
        }

        user = User.objects.create_user(**user_data)
        return {"user": user, "user_data": user_data}

    return _make_db_user


@pytest.fixture()
def make_user_registration(register_user, api_client):
    return api_client.post(
        "/api/auth/register/",
        register_user,
    )


@pytest.fixture()
def login_user(api_client, make_db_user):
    db_user = make_db_user()
    response = api_client.post(
        "/api/auth/login/",
        {
            "email": db_user["user_data"]["email"],
            "password": db_user["user_data"]["password"],
        },
    )
    return response


@pytest.fixture()
def superusers_factory():
    def _superuser_factory(make_db_user):
        return make_db_user

    return _superuser_factory
