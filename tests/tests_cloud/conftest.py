import io
import os
import uuid

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from djangoProject import test_settings as settings


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
    file_path = os.path.join(settings.STATIC_ROOT, file_name)
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
    def _upload_file(api_client, login_user, mock_file_api):
        response = api_client.post(
            "/api/cloud/files/",
            headers={
                "Authorization": "Bearer " + login_user.data["access"],
            },
            data=mock_file_api(),
            format="multipart",
        )
        return response

    return _upload_file
