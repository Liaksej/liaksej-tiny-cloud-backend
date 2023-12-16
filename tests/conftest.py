import io
import os
import uuid

import pytest
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker
from rest_framework.test import APIClient

from djangoProject import test_settings as settings


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(name="faker")
def users_factory():
    return Faker()


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
def login_user(make_db_user, api_client):
    db_user = make_db_user()
    response = api_client.post(
        "/api/auth/login/",
        {
            "email": db_user["user_data"]["email"],
            "password": db_user["user_data"]["password"],
        },
    )
    return response


@pytest.fixture
def mock_file_services(mocker, file_content="file content"):
    def _file_mock():
        file_mock = mocker.MagicMock(spec=SimpleUploadedFile)
        file_mock.chunks.return_value = [file_content]
        file_mock.name = "test.txt"
        return file_mock

    return _file_mock


@pytest.fixture
def file_path_and_name():
    file_name = f"{uuid.uuid4().hex}.txt"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    return file_path, file_name


@pytest.fixture
def mock_file_api():
    def _mock_file_api():
        mock_file = io.BytesIO(
            b"\x50\x6F\x77\x65\x72\x50\x6F\x69\x6E\x74\x20\x44\x6F\x63\x75\x6D\x65\x6E\x74"
        )
        mock_file.name = "test.txt"
        data = {
            "file": mock_file,
            "file_name": "test.txt",
            "comment": "some comment",
        }
        return data

    return _mock_file_api


@pytest.fixture
def upload_file():
    file_name = None

    def _upload_file(api_client, user, mock_file_api):
        nonlocal file_name
        response = api_client.post(
            "/api/cloud/files/",
            headers={
                "Authorization": "Bearer " + user.data["access"],
            },
            data=mock_file_api(),
            format="multipart",
        )
        file_name = response.data["name"]
        return response

    yield _upload_file
    if file_name and os.path.exists(os.path.join(settings.MEDIA_ROOT, file_name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, file_name))


@pytest.fixture
def file_list():
    def _file_list(api_client, make_user_registration):
        return api_client.get(
            "/api/cloud/files/",
            headers={
                "Authorization": "Bearer " + make_user_registration.data["access"],
            },
        )

    return _file_list


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


@pytest.fixture
def login_superuser(make_db_user, api_client):
    superuser = make_db_user()

    return api_client.post(
        "/api/auth/login/",
        data={
            "email": superuser["user_data"]["email"],
            "password": superuser["user_data"]["password"],
        },
    )
