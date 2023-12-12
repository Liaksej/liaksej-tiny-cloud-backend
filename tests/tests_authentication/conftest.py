import pytest


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


@pytest.fixture()
def make_user_registration(register_user, api_client):
    return api_client.post(
        "/api/auth/register/",
        register_user,
    )


@pytest.fixture()
def superusers_factory():
    def _superuser_factory(make_db_user):
        return make_db_user

    return _superuser_factory
