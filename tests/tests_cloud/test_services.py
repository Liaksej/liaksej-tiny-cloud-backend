import pytest

from cloud.services import (
    save_file,
    delete_file,
)


def test_save_file(mocker, file_path_and_name, mock_file_services):
    """Test api endpoint for save file function"""

    file_mock = mock_file_services()

    mocker.patch("builtins.open", mocker.mock_open())
    mocker.patch("os.path.join", return_value=file_path_and_name[0])

    uuid_mock = mocker.MagicMock()
    uuid_mock.hex = file_path_and_name[1].split(".")[0]
    mocker.patch("uuid.uuid4", return_value=uuid_mock)
    mocker.patch("os.path.splitext", return_value=("", ".txt"))

    result = save_file(file_mock(mocker))

    file_path, file_name = file_path_and_name
    assert result == {"file_name": file_name, "file_path": file_path}


@pytest.mark.parametrize(
    "file_path, should_raise",
    [
        ("file_path", False),
        ("non_existent_file_path", True),
    ],
)
def test_delete_file(mocker, file_path, should_raise):
    """Test api endpoint for delete file function"""

    mock_remove = mocker.patch(
        "os.remove", side_effect=FileNotFoundError if should_raise else None
    )
    delete_file(file_path)

    mock_remove.assert_called_once_with(file_path)
